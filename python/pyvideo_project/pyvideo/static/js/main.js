$(document).ready(function(){

    $("input[id^='video_check-']").each(function(){
        $(this).click(function() {
            if($(this).prop('checked') == true){
                $('#video_delete_btn').toggleClass('disabled', false);
                if(all_input_checked()){
                    $('#video_checkall').prop('checked', true);
                    $('#video_checkall').prop('indeterminate', false);
                }else{
                    $('#video_checkall').prop('indeterminate', true);
                }
            }
            else{
                if(no_input_checked() == true){
                    $('#video_delete_btn').toggleClass('disabled', true);
                    $('#video_checkall').prop('checked', false);
                    $('#video_checkall').prop('indeterminate', false);
                }else{
                    $('#video_checkall').prop('indeterminate', true);
                }
            }
        });
    });

    $("#video_checkall").click(function(){
        if($(this).prop('checked')){
            set_all_input(true);
        }else{
            set_all_input(false);
        }
        $(this).prop('indeterminate', false);
    });


    function no_input_checked(){
        var no_checked = true;
        $("input[id^='video_check-']").each( function(){
            if($(this).prop('checked') == true){
                no_checked = false;
            }
        });
        return no_checked
    }

    function all_input_checked(){
        all_checked = true;
        $("input[id^='video_check-']").each( function(){
            if($(this).prop('checked') == false){
                all_checked = false;
            }
        });
        return all_checked;
    }

    function set_all_input(state){
        $("input[id^='video_check-']").each(function(){
            $(this).prop('checked', state)
        });
    }

    $("#video_delete_btn").click(function(){
        $("#video_form").prop('action', '/delete_video');
        $("#video_form").prop('method', 'post');
        $("#video_form").submit();
    });

    $("#video_search_btn").click(function(){
        $("#video_form").prop('action', '/search_video');
        $("#video_form").prop('method', 'get');
        $("#video_form").submit();

    });

});
