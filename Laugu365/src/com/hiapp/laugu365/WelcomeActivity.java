package com.hiapp.laugu365;

import com.hiapp.util.NetworkManager;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.os.Handler;
import android.os.Message;
import android.content.DialogInterface;
import android.content.Intent;

public class WelcomeActivity extends Activity implements Runnable{

	@Override
	protected void onCreate(Bundle saveInstanceState){
		super.onCreate(saveInstanceState);
		
		//1.设置无标题窗口
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		//2.设置窗体全屏
		getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
		//3.设置当前activity的布局
		setContentView(R.layout.welcome);
		//4.获取网络管理工具
		NetworkManager netManager = NetworkManager.getInstance(getApplicationContext());
		//5.根据网络连接状况决定启动应用
		if(netManager.isMobileNetwork(getApplicationContext())&&netManager.network_accessable(getApplicationContext())){
			//5.1如果网络可用
			new Thread(this).start();
		}else{
			//5.2如果网络不可用
			final AlertDialog.Builder builder = new AlertDialog.Builder(WelcomeActivity.this);
			builder.setTitle(R.string.no_network_alert_title)   //设置提示框标题
			       .setMessage(R.string.no_network_alert_msg)   //设置提示信息
			       .setPositiveButton(R.string.no_network_alert_tips, new DialogInterface.OnClickListener() {					
					@Override
					public void onClick(DialogInterface dialog, int which) {
						android.os.Process.killProcess(android.os.Process.myPid());	
						System.exit(0);
					}
				}); //设置提示框确认建，确认后杀死进程，退出程序;
		}
	}
	@Override
	public void run() {
		try{
			 Thread.sleep(2000);
		}catch(InterruptedException e){
			e.printStackTrace();
		}
		myHandler.sendEmptyMessage(0);
	}
	
	private Handler myHandler = new Handler(){
		public void handleMessage(Message msg){
			if(msg.what==0){
				WelcomeActivity.this.finish();
				startActivity(new Intent(WelcomeActivity.this,Laugh365Activity.class));
			}
		}
	};

}
