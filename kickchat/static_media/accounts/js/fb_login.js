// Additional JS functions here
function fbAsyncInit() {
    console.log('calling');
    FB.init({
        appId      : '391575564302792', // App ID
        channelUrl : '', // Channel File
        status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
        xfbml      : true  // parse XFBML
    });
    FB.Event.subscribe('auth.authResponseChange', function(response) {
        console.log(response);
        if (response.status === 'connected') {
            testAPI();
            if (access_token_sent === false) {
                sendToken();
                access_token_sent = true;
            }
        } else {
            FB.login();
        }
    });
}

// Load the SDK asynchronously
(function(d){
    var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement('script'); js.id = id; js.async = true;
    js.src = "//connect.facebook.net/en_US/all.js";
    ref.parentNode.insertBefore(js, ref);
}(document));

function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
        console.log('Good to see you, ' + response.name + '.');
    });
}

$('#fb-connect').click(function(){
    console.log('a');
    var access_token_sent = false;
    
});
