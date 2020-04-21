$(document).ready(function(){
	setTimeout(createButton, 3000)
})

drp = `<style>
				.dropbtn {
				  background-color: initial;
				  color: #595959;
				  cursor: pointer;
				}

				.dropdown {
					margin:auto;
					margin-right:15px;
				  position: relative;
				}

				.dropdown-content {
					right: 0;
				  display: none;
				  position: absolute;
				  font-size: 12px;
				  background-color: #ededed;
				  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
				  z-index: 1;
				}

				.dropdown-content a {
				  color: black;
				  padding: 12px 20px;
				  text-decoration: none;
				  display: block;
				}

				.dropdown-content a:hover {
					background-color: #727171;
					color: #ededed;
				}

				.dropdown:hover .dropdown-content {
				  display: block;
				}

				.dropdown:hover .dropbtn {
				  color: #3e8e41;
				}
			</style>

			<div class="dropdown">
				<i class="fa fa-download fa-2x dropbtn" aria-hidden="true"></i>
				<div class="dropdown-content">
				  <a id='mp3' href="#">mp3</a>
				  <a id='mp4' href="#">mp4</a>
			  </div>
			</div>`


function createButton(){
	$('#top-level-buttons').prepend(drp)
	var url = location.href
	var video_id = url.split('=')[1]
	

	var port = chrome.runtime.connect({name: video_id})
	port.onMessage.addListener(function(msg){
		if (msg.success){
			$('#mp3').attr('href', msg.links.MP3)
			$('#mp4').attr('href', msg.links.MP4)
			$('.dropbtn').css({color: '#00cc00'});
		} else {
			$('.dropbtn').css('color', 'red')
		}
	})
}

