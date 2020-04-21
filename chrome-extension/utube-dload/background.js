chrome.runtime.onConnect.addListener(function(port){
	vid = port.name

  jQuery.ajax({
	url: 'https://utube-dload.herokuapp.com/',
	type: 'POST',
	data: {'video_id': vid},
  success: function(resp_data){
  		port.postMessage({success: true, links: resp_data})
  	}
	})
	.done(function() {
		console.log('Success')
	})
	.fail(function() {
		console.log('Failed')
	})
})



















