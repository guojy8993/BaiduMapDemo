package com.hiapp.laugu365;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;

public class AboutActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_about);
		findViewById(R.id.about_back_btn).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				AboutActivity.this.finish();
			}
		});
	}
}
