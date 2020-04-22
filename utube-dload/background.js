chrome.runtime.onConnect.addListener(function(port){
	vid = port.name

  jQuery.ajax({
	url: 'https://utube-dload.herokuapp.com/',
	type: 'POST',
	data: {'video_id': vid},
  success: function(resp_data){
  	if (resp_data.success){
  		port.postMessage({success: true, links: resp_data})
  	} else {
  		port.postMessage({success: false})
  	}
  	}
	})
	.done(function() {
		console.log('Success')
	})
	.fail(function() {
		console.log('Failed')
	})
})

chrome.browserAction.onClicked.addListener(function(tab){
	let msg = {
		task: 'reload'
	}
	chrome.tabs.sendMessage(tab.id, msg)
	console.log('Reloading links.')
})



















