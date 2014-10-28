package com.hiapp.laugu365;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import net.youmi.android.AdView;

import android.app.Activity;
import android.app.AlertDialog;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup.LayoutParams;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.GridView;
import android.widget.Button;
import android.widget.TextView;
import android.widget.ImageView;
import android.widget.BaseAdapter;
import android.app.ProgressDialog;
import android.widget.LinearLayout;
import android.widget.AdapterView.OnItemClickListener;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Message;
import android.os.Handler;
import android.content.Context;

public class ImageActivity extends Activity{
	
	private GridView gridView ;
	
	private Button back;
	private TextView title;
	
	private String page_url_1 ;
	private String name;
	
	private int page = 1;
	private String flag;
	
	private ImageAdapter imageAdapter;
	private ProgressDialog progressDialog;
	
	private ArrayList<String> mIMageUrls = new ArrayList<String>();
	private ArrayList<String> mImageName = new ArrayList<String>();
	private ArrayList<String> mImageName2 = new ArrayList<String>();
	
	@Override
	protected void onCreate(Bundle saveInstanceBundle){
		super.onCreate(saveInstanceBundle);
		setContentView(R.layout.image_activity);
		LinearLayout ll = (LinearLayout)findViewById(R.id.image_bottom);
		ll.addView(new AdView(this),new LayoutParams(LinearLayout.LayoutParams.FILL_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT));
		
		gridView = (GridView)findViewById(R.id.image_gridview);
		title = (TextView)findViewById(R.id.image_title_text);
		back = (Button)findViewById(R.id.image_back);
		gridView.setOnItemClickListener(listener);
		
		imageAdapter = new ImageAdapter();
		progressDialog = new ProgressDialog(this);		
		progressDialog.setMessage("加载中......");
		
		Intent it = getIntent();
		name = it.getStringExtra("title");
		title.setText(name);
		if(name.equals("animal_comic")){
			page_url_1 = "http://www.laifu.org/tupian/dongwutupian.htm";
			flag = "dongwutupian";
		}else if(name.equals("children")){
			page_url_1 = "http://www.laifu.org/tupian/dongwutupian.htm";
			flag = "dongwutupian";
		}else if(name.equals("fool")){
			page_url_1 = "http://www.laifu.org/tupian/dongwutupian.htm";
			flag = "dongwutupian";
		}else if(name.equals("interestings")){
			page_url_1 = "http://www.laifu.org/tupian/dongwutupian.htm";
			flag = "dongwutupian";
		}
		progressDialog.show();
		new Thread(){
			public void run(){
				try{
					Document doc = Jsoup.connect(page_url_1).get();
					Elements es = doc.select(".picListTable img");
					for(int i=0;i<es.size();i++){
						String image_url = es.get(i).attr("src");
						String name = es.get(i).attr("alt");
						mImageName2.add(name);
						if(name.length()>8){
							name = name.subSequence(0, 8).toString();	
						}
						mImageName.add(name);
						mIMageUrls.add(image_url);
						Message msg = new Message();
						msg.what = 1;
						myHandler.sendMessage(msg);
					}
				}catch(IOException e){
					Message msg = new Message();
					msg.what = 2;
					myHandler.sendMessage(msg);
				}
			}
		}.start();
		
		back.setOnClickListener(new OnClickListener(){

			@Override
			public void onClick(View arg0) {
				ImageActivity.this.finish();				
			}			
		});
	}
	private Handler myHandler = new Handler(){
		public void handleMessage(Message msg){
			switch(msg.what){
			case 1:
				progressDialog.cancel();
				gridView.setAdapter(imageAdapter);
				break;
			case 2:
				progressDialog.cancel();
				final AlertDialog.Builder builder = new AlertDialog.Builder(ImageActivity.this);
				builder.setTitle(R.string.ex_occured_while_loading_pics)
				       .setMessage(R.string.msg_disp_when_error)
				       .setPositiveButton(R.string.main_back_alert_confirm, new DialogInterface.OnClickListener() {
						
						@Override
						public void onClick(DialogInterface arg0, int arg1) {
							android.os.Process.killProcess(android.os.Process.myPid());	
							System.exit(0);
						}
					}).create().show();
				break;
			case 3:
				progressDialog.cancel();
				imageAdapter.notifyDataSetChanged();
				break;
			}
		}
	};
	private OnItemClickListener listener = new OnItemClickListener(){

		@Override
		public void onItemClick(AdapterView<?> arg0, View arg1, int arg2,long arg3) {
			int count = imageAdapter.getCount();
			if(arg2 == count-1){
				page++;
				final String nextPage = "http://www.laifu.org/tupian/"+flag+"_"+page+".htm";
				progressDialog.show();
				new Thread(){
					public void run(){
						try{
							Document doc = Jsoup.connect(nextPage).get();
							Elements es = doc.select(".picListTable img");
							for(int i=0;i<es.size();i++){
								String image_url = es.get(i).attr("src");
								String name = es.get(i).attr("alt");
								mImageName2.add(name);
								if(name.length()>8){
									name = name.substring(0,8).toString();
								}
								mImageName2.add(name);
								mIMageUrls.add(image_url);
								Message msg = new Message();
								msg.what = 3;
								myHandler.sendMessage(msg);
							}
						}catch(IOException e){
							Message msg = new Message();
							msg.what = 2;
							myHandler.sendMessage(msg);
						}
					}
				}.start();
				return ;
			}
			Intent it = new Intent(ImageActivity.this,ImageReadActivity.class);
			it.putExtra("name", name);
			it.putExtra("article_name", mImageName2.get(arg2));
			it.putExtra("article_url", mIMageUrls.get(arg2));
			startActivity(it);
		}		
	};
	private class ImageAsyncTask extends AsyncTask<String,Integer,Bitmap>{
		private ImageView iv = null;
		public ImageAsyncTask(Context context,ImageView iv){
			this.iv = iv;
		}
		@Override
		protected Bitmap doInBackground(String... params) {
			String s = params[0];
			URL url = null;
			HttpURLConnection conn = null;
			InputStream is = null;
			try{
				url = new URL(s);
				conn = (HttpURLConnection)url.openConnection();
				is = conn.getInputStream();
				return BitmapFactory.decodeStream(is);
			}catch(Exception e){
				e.printStackTrace();
			}finally{
				try{
					if(is != null){
						is.close();
					}
					if(conn != null){
						conn.disconnect();
					}
				}catch(IOException e){
					e.printStackTrace();
				}
			}
			return null;
		}
		
		@Override
		protected void onPostExecute(Bitmap result){
			if(result !=null){
				iv.setImageBitmap(result);
			}
			super.onPostExecute(result);
		}		
	}
	class ImageAdapter extends BaseAdapter{

		@Override
		public int getCount() {
			return mImageName.size()+1;
		}

		@Override
		public Object getItem(int arg0) {
			return arg0;
		}

		@Override
		public long getItemId(int arg0) {
			return 0;
		}

		@Override
		public View getView(int position, View convertView, ViewGroup parent) {
			ViewHolder holder = null;
			convertView = View.inflate(getApplicationContext(), R.layout.item2, null);
			holder = new ViewHolder();
			holder.text = (TextView) convertView.findViewById(R.id.text);
			holder.image = (ImageView) convertView.findViewById(R.id.image);
			if(position == mImageName.size()){
				holder.text.setText("");
				holder.image.setImageResource(R.drawable.add_section);
				return convertView;
			}
			holder.text.setText(mImageName.get(position));
			ImageAsyncTask task = new ImageAsyncTask(ImageActivity.this,holder.image);
			task.execute(mIMageUrls.get(position));
			return convertView;
		}
		class ViewHolder{
			private ImageView image;
			private TextView text;
		}
		
	}
}
