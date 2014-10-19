package com.hiapp.util;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;

public class NetworkManager {

	private static NetworkManager networkManager ;
	private NetworkManager(){
		
	}
	public static NetworkManager getInstance(final Context context){
		if(networkManager==null){
			networkManager = new NetworkManager();
		}
		return networkManager;
	}
	//判断当前网络可用状态
	public boolean network_accessable(Context context){
		ConnectivityManager connManager = (ConnectivityManager)context.getSystemService(Context.CONNECTIVITY_SERVICE);
		NetworkInfo network_info = connManager.getActiveNetworkInfo();
		if(network_info!=null&&network_info.isAvailable()) return true;
		return false;
	}
	//判断是否是手机网络
	public boolean isMobileNetwork(Context context){
		ConnectivityManager connManager = (ConnectivityManager)context.getSystemService(Context.CONNECTIVITY_SERVICE);
		NetworkInfo network_info = connManager.getActiveNetworkInfo();
		if(network_info!=null&&network_info.getType()==ConnectivityManager.TYPE_MOBILE) return true;
		return false;
	}
}
