function load_pagelets() {
    console.log(data.count);
    for(var i =1; i <= count ; i++)
    {
        var element_id = 'ID_' + i;
        //console.log(data.ids[element_id]);
        $.ajax({
            url: pagelets[],
            success: function(html) {
                var html_element = $('#' + data.ids[element_id]);
                console.log(html_element)
                html_element.html(html);
            }
        });
    }
}
$(document).ready(function(){
    load_pagelets();
});