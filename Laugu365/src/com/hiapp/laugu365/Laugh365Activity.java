package com.hiapp.laugu365;

import net.youmi.android.AdManager;
import android.app.Activity;
import android.app.AlertDialog;
import android.os.Bundle;
import android.view.View;
import android.view.MenuInflater;
import android.view.ViewGroup;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.AdapterView;
import android.widget.GridView;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.AdapterView.OnItemClickListener;
import android.content.DialogInterface;
import android.content.Intent;
import android.view.KeyEvent;

public class Laugh365Activity extends Activity {

	private GridView gridView;
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		AdManager.init(getApplicationContext(), "c1ced68cd9b2f3bd", "fc83ab5311ddbf2a", 100, false);
		setContentView(R.layout.laugh365);
		
		gridView = (GridView)this.findViewById(R.id.content_view_by_class);
		gridView.setAdapter(new ImageAdapter());
		gridView.setOnItemClickListener(listener);
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu){
		MenuInflater menuInflater = getMenuInflater();
		menuInflater.inflate(R.layout.main_menu, menu);
		return super.onCreateOptionsMenu(menu);
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem menuItem){
		switch(menuItem.getItemId()){
		case R.id.about:
			startActivity(new Intent(Laugh365Activity.this,AboutActivity.class));
			return true;
		}
		return super.onOptionsItemSelected(menuItem);
	}
	@Override
	public boolean onKeyDown(int keyCode,KeyEvent keyEvent){
		if(keyCode == KeyEvent.KEYCODE_BACK){
			AlertDialog.Builder builder = new AlertDialog.Builder(Laugh365Activity.this);
			builder.setTitle(R.string.main_back_alert_title)
			       .setMessage(R.string.main_back_alert_msg)
			       .setPositiveButton(R.string.main_back_alert_confirm, new DialogInterface.OnClickListener(){

						@Override
						public void onClick(DialogInterface dialog, int which) {
							Laugh365Activity.this.finish();
							android.os.Process.killProcess(android.os.Process.myPid());
							android.os.Process.killProcess(android.os.Process.myTid());
							android.os.Process.killProcess(android.os.Process.myUid());
						}				    	   
				    })
			      .setNegativeButton(R.string.main_back_alert_cancel,new DialogInterface.OnClickListener(){

						@Override
						public void onClick(DialogInterface dialog, int which) {							
							dialog.cancel();
						}
				
			});
			builder.show();
			return true;
		}
		return super.onKeyDown(keyCode, keyEvent);
				
	}
	private OnItemClickListener listener = new OnItemClickListener(){

		@Override
		public void onItemClick(AdapterView<?> parent, View view, int position,long id) {
			switch(position){
			case 0:
				    Intent animal_comic = new Intent(getApplicationContext(),ImageActivity.class);
				    animal_comic.putExtra("title", "animal_comic");
				    startActivity(animal_comic);
				    break;
			case 1:
				    Intent children = new Intent(getApplicationContext(),ImageActivity.class);
				    children.putExtra("title", "children");
				    startActivity(children);
				    break;
			case 2:
				    Intent fool = new Intent(getApplicationContext(),TextActivity.class); 
				    fool.putExtra("title", "fool");
				    startActivity(fool);
				    break;
			case 3:
				    Intent interestings = new Intent(getApplicationContext(),TextActivity.class);
				    interestings.putExtra("title", "interestings");
				    startActivity(interestings);
				    break;
			}			
		}
		
	};
	//内部类专门服务于 Laugh365Activity 
	private class ImageAdapter extends BaseAdapter{

		@Override
		public int getCount() {
			//ImageAdapter getCount()/numColumns e.g: 5/2=2..1 即为3行
			return ids.length;
		}

		@Override
		public Object getItem(int position) {			
			return null;
		}

		@Override
		public long getItemId(int position) {			
			return 0;
		}

		@Override
		public View getView(int position, View convertView, ViewGroup parent) {
			ViewHolder holder = null;
			if(convertView == null){
				convertView = View.inflate(getApplicationContext(), R.layout.item,null);
				holder = new ViewHolder();
				holder.text = (TextView)convertView.findViewById(R.id.text);
				holder.image = (ImageView)convertView.findViewById(R.id.image);
				convertView.setTag(holder);
			}else{
				holder = (ViewHolder)convertView.getTag();
			}
			holder.text.setText(titles[position]);
			holder.image.setImageResource(ids[position]);
			return convertView;
		}
		
		class ViewHolder{
			TextView text;
			ImageView image;
		}		
		private int[] ids = {R.drawable.main_pic_0,R.drawable.main_pic_1,R.drawable.main_pic_2,R.drawable.main_pic_3};
		private int[] titles = {R.string.animal_and_comic,R.string.children,R.string.fool,R.string.interestings};
	}
}
