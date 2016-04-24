// function $(id){
// 	return typeof id==='string'?document.getElementById(id):id;
// }

// window.onload=function(){
// 	//获取鼠标点击的标签和要切换的内容
// 	var titles=$('notice-tit').getElementsByTagName('li');
// 	//遍历titles下的所有li
// 	for(var i=0;i<titles.length;i++){
// 		titles[i].id=i;
// 		titles[i].onclick=function(){
// 			//清除所有li上的class
// 			for(var j=0;j<titles.length;j++){
// 				titles[j].className='';
// 			}
// 			//设置当前class
// 			this.className='select';
// 		}
// 	}
// }

// window.onload=function(){
// 	//获取鼠标点击的标签和要切换的内容
// 	var titles=$('notice-tit').getElementsByTagName('li');
// 	var alink=$('notice-tit').getElementsByTagName('a');
// 	var divs=$('notice-con').getElementsByTagName('div');
// 	//遍历titles下的所有li
// 	for(var i=0;i<titles.length;i++){
// 		alink[i].id=i;
// 		alink[i].onclick=function(){
// 			//清除所有li上的class
// 			for(var j=0;j<titles.length;j++){
// 				titles[j].className=' ';
// 				divs[j].style.display='none';
// 			}
// 			//设置当前class
// 			titles[this.id].className='select';
// 			divs[this.id].style.display='block';
// 		}
// 	}
// }

$(document).ready(function() {
	//获取鼠标点击的标签和要切换的内容
	var titles=$('.liclass');
	var alink=$('.aclass');
	var divs=$('.mod');
	//遍历titles下的所有li
	for(var i=0;i<titles.length;i++){
		titles[i].id=i;
		titles[i].onclick=function(){
			//清除所有li上的class
			titles.removeClass('select');
			divs.hide();
			//设置当前class
			this.className='select';
			divs[5-(this.id)].style.display="block";
		}
	}
});