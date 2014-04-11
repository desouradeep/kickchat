$(document).ready(function(){
    $(window).resize(function(){
        
        // Chat Table resize
        var window_height = $(window).height();
        var navbar_height = 60;
        var message_box_height = 40;
        var message_container_height = window_height - navbar_height - message_box_height;
        message_column_id="#message-column";
        $(message_column_id).height(message_container_height);
        console.log(message_container_height);

        // Chat Input group resize
        var chat_input_group_width = $('#message-column').width();
        var chat_submit_button_width = $('#chat-submit-button').width();
        var chat_input_width = chat_input_group_width - chat_submit_button_width;
        console.log(chat_input_width);
        $('#chat-input').width(chat_input_width - 50);
    });
    $(window).resize();


    // Scroll to the bottom of messages
    function scroll_down() {
        var messages_container_height = $('#messages-container').height();
        $('#message-column').scrollTop(messages_container_height);
    }
    scroll_down();
});