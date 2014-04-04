$(document).ready(function(){
    function set_message_box_height () {
        var window_height = $(window).height();
        var navbar_height = 70;
        var message_box_height = 50;
        var message_container_height = window_height - navbar_height - message_box_height;
        message_container_id="#messages-container";
        $(message_container_id).height(message_container_height);
    }
});