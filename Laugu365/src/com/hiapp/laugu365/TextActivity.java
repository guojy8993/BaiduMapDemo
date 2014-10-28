package com.hiapp.laugu365;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Button;
import android.widget.ListView;
import android.app.ProgressDialog;
import java.util.ArrayList;
import android.os.Bundle;
import android.widget.BaseAdapter;
import android.widget.ImageView;

public class TextActivity extends Activity{

	private TextView title;
	private Button back;
	private ListView mView;
	
	private String name;
	private String url = "http://www.laifu.org";
	private String pageUrl_1;
	private int page = 1;
	private String tag;
	
	private ProgressDialog progressDialog;
	private MyAdapter mAdapter;
	
	private ArrayList<String> mList = new ArrayList<String>();
	private ArrayList<String> mUrls = new ArrayList<String>();
	
	protected void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_text);
	}
	private class MyAdapter extends BaseAdapter{

		@Override
		public int getCount() {
			// TODO Auto-generated method stub
			return mList.size();
		}

		@Override
		public Object getItem(int arg0) {
			// TODO Auto-generated method stub
			return arg0;
		}

		@Override
		public long getItemId(int arg0) {
			// TODO Auto-generated method stub
			return 0;
		}

		@Override
		public View getView(int position, View converView, ViewGroup parent) {
			ViewHolder holder = null;
			if(converView == null){
				converView = View.inflate(getApplicationContext(),R.layout.item_text, null);
				holder = new ViewHolder();
				holder.image = (TextView)converView.findViewById()
			}
			return null;
		}
		class ViewHolder{
			ImageView image;
		}
		
	}
}
