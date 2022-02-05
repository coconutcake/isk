


(function($) {
    $.fn.extend({
        DjangoAjaxForm: function(options) {
            var defaults = {
                method: "POST",
                data: {},
                additional_data:{},
                form: "",
                url: "",
                headers: {
                    "X-CSRFToken": '{{ csrf_token }}',
                    "X-Requested-With": "XMLHttpRequest"
                },
            };

            options = $.extend(defaults, options);
            
            let $submit_button_class = $(this).attr("submit_button_class");
            let $form_id = $(this).attr("id");
            let $submit_button = $("."+$submit_button_class+"[form="+$form_id+"]")

            $submit_button.on("click",function(){
                // Data collection
                console.log("Collecting data from form: "+$form_id+" ...")
                options['form'] = $form_id
                let $form = $("#"+options['form'])
                options['url'] = $form.attr("action")
                options['method'] = $form.attr("method")
                options['success'] = $form.attr("success_redirect")
                options['paste_content_success'] = $form.attr("paste_content_success")
                options['paste_content_failed'] = $form.attr("paste_content_failed")
                options['headers']['X-CSRFToken'] = $form.attr("csrf_token")
                options['data'] = {"form_data":$form.serialize()}
                options['data']['additional_data'] = $.param(options.additional_data)
                console.log("Collected data: \nurl: "+options['url']+", \nform:"+options['form']+", \nmethod: "+options['method']+", \ndata: "+JSON.stringify(options['data'])+", \nheaders: "+JSON.stringify(options['headers'])+", \nsuccess redirect to: "+options['success_redirect']+", \npaste content on success to: "+options['paste_content_success'])
                console.log("Performing "+options['method']+" request...")
                // Ajax
                $.ajax({
                    url: options['url'],
                    type: options['method'],
                    data: options['data'],
                    headers: options['headers'],
                    success: function(data){
                        console.log("Success!")
                        console.log(data)
                        $(options['paste_content_failed']).empty().html(data);
                        }
                });
            })
}
});
})(jQuery);


(function($) {
    $.fn.extend({
        LoadRemoteContent: function(options) {
            var defaults = {
                method: "GET",
                url: "",
                paste_content_to: $(this),
                headers: {
                    "X-CSRFToken": '{{ csrf_token }}',
                    "X-Requested-With": "XMLHttpRequest"
                },
            };


            options = $.extend(defaults, options);

            $.get(options['url'], function(data) {
                $(options['paste_content_to']).html(data);
                console.log("Form loaded!")
            });

        }
    });
    })(jQuery);

(function($) {
    $.fn.extend({
        DjangoSingleAjaxForm: function(options) {
            var defaults = {
                method: "POST",
                data: {},
                additional_data:{},
                form: "",
                url: "",
                status_success_animation: "green-animation",
                headers: {
                    "X-CSRFToken": '{{ csrf_token }}',
                    "X-Requested-With": "XMLHttpRequest"
                },
            };
            options = $.extend(defaults, options);
            console.log("Executing DjangoSingleAjaxForm plugin...")
            let $submit_button_class = $(this).attr('submit_button_class');
            let $form_id = $(this).attr("id");
            let $submit_button = $("."+$submit_button_class+"[form="+$form_id+"]")

            function status_success_show(form,data){
                let $form = form
                $(options['status_html']).css("display","inline").show()
                var es = $(options['status_html']).empty().html(data.status_html).show();
                setTimeout(function() {
                    es.fadeOut(2500)
                }, 500);

                var el = $form.find('input, textarea, select').addClass(options['status_success_animation']);
                setTimeout(function() {
                    el.removeClass(options['status_success_animation']);
                }, 3000);
            }


            function delete_errors(form){
                let $form = form
                $form.find("ul.errorlist").remove()
            }

            $submit_button.on("click",function(){
                console.log("Collecting data from form: "+$form_id+" ...")
                options['form'] = $form_id
                let $form = $("#"+options['form'])
                options['url'] = $form.attr("action")
                options['method'] = $form.attr("method")
                options['success'] = $form.attr("success_redirect")
                options['status_html'] = $form.attr("status_html")
                options['data'] = {"form_data":$form.serialize()}
                options['data']['additional_data'] = $.param(options.additional_data)
                console.log("Collected data: \nurl: "+options['url']+", \nform:"+options['form']+", \nmethod: "+options['method']+", \ndata: "+JSON.stringify(options['data'])+", \nheaders: "+JSON.stringify(options['headers'])+", \nsuccess redirect to: "+options['success_redirect']+", \npaste content on success to: "+options['paste_content_success'])
                console.log("Performing "+options['method']+" request...")
                // Ajax
                $.ajax({
                    url: options['url'],
                    type: options['method'],
                    data: options['data'],
                    success: function(data){
                        if (data.status == 201){
                            console.log("CREATED!")
                            console.log(data.status_html)
                            status_success_show($form,data)
                            delete_errors($form)
                        }
                        if (data.status == 400){
                            console.log("FAILED!")
                            console.log(data)
                            $form.parent().parent().parent().empty().html(data.form_string_html);
                        }
                        }
                });
            })
}
});
})(jQuery);

(function($) {
    $.fn.extend({
        DjangoSearchForm: function(options) {
            var defaults = {
                method: "GET",
                data: {},
                additional_data:{},
                form: "",
                url: "",
                headers: {
                    "X-CSRFToken": '{{ csrf_token }}',
                    "X-Requested-With": "XMLHttpRequest"
                },
            };

            options = $.extend(defaults, options);
            
            let $submit_button_class = $(this).attr("submit_button_class");
            let $form_id = $(this).attr("id");
            let $submit_button = $("."+$submit_button_class+"[form="+$form_id+"]")

            $submit_button.on("click",function(){
                // Data collection
                console.log("Collecting data from form: "+$form_id+" ...")
                options['form'] = $form_id
                let $form = $("#"+options['form'])
                options['url'] = $form.attr("action")
                options['method'] = $form.attr("method")
                options['success'] = $form.attr("success_redirect")
                options['paste_content_success'] = $form.attr("paste_content_success")
                options['headers']['X-CSRFToken'] = $form.attr("csrf_token")
                options['data'] = {"form_data":$form.serialize()}
                options['data']['additional_data'] = $.param(options.additional_data)
                console.log("Collected data: \nurl: "+options['url']+", \nform:"+options['form']+", \nmethod: "+options['method']+", \ndata: "+JSON.stringify(options['data'])+", \nheaders: "+JSON.stringify(options['headers'])+", \nsuccess redirect to: "+options['success_redirect']+", \npaste content on success to: "+options['paste_content_success'])
                console.log("Performing "+options['method']+" request...")
                let searchParams = window.location.href

                let $u = options['data']['form_data'].split("&") // <- posiekaj w liste
                delete $u[0] // <- usun pierwszy element (token)
                let $c = $u.join('&') // <- polacz ze znakiem &
                const $uriparams = '?' + $c.substring(1); // <- zamien pierwszy & na search?
                
                window.location.replace(options['url']+$uriparams);
            })
}
});
})(jQuery);