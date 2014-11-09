package com.apps.baidumap;

import com.apps.baidumap.R;
import com.baidu.mapapi.SDKInitializer;
import com.baidu.mapapi.map.MapView;

import android.app.Activity;
import android.os.Bundle;

public class DemoMain extends Activity{
	MapView mapView = null;
	@Override
	protected void onCreate(Bundle savedInstance){
		super.onCreate(savedInstance);
		SDKInitializer.initialize(getApplicationContext());
		setContentView(R.layout.demomain);
		mapView = (MapView)findViewById(R.id.main_mapview);
	}
	@Override
	protected void onDestroy(){
		super.onDestroy();
		mapView.onDestroy();
		mapView.onDestroy();
	}
	@Override
	protected void onResume(){
		super.onResume();
		mapView.onResume();
	}
	@Override
	protected void onPause(){
		super.onPause();
		mapView.onPause();
	}
	
}
