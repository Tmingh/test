$(document).ready(function() {
	var secalink=$('.sec-aclass');
	var secdivs=$('.pro');
	for(var i=0;i<secalink.length;i++){
		secalink[i].id=i;
		secalink[i].onclick=function(){
			secalink.removeClass('sec-select');
			secdivs.hide();
			this.className='sec-select';
			secdivs[this.id].style.display="block";
		}
	}
});