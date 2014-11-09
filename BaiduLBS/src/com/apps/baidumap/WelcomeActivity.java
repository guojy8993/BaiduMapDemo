package com.apps.baidumap;

import com.apps.baidumap.R;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Window;
import android.view.WindowManager;

public class WelcomeActivity extends Activity implements Runnable{
	private static final String TAG = "WelcomeActivity";
	@Override
	protected void onCreate(Bundle saveInstance){
		super.onCreate(saveInstance);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
		setContentView(R.layout.welcome);
		new Thread(this).start();
	}

	@Override
	public void run() {
		try{
			Thread.sleep(2000);
			Intent toMain = new Intent(getApplicationContext(),DemoMain.class);
			startActivity(toMain);
		}catch(InterruptedException ie){
			Log.i(TAG,ie.getLocalizedMessage());
			Thread.currentThread().interrupt();
		}
	}
}
