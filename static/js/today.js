// Ajax Django csrf
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(function(){
	$.ajaxSetup({
		headers: {'X-CSRFToken': csrftoken}
	});
});

// Models

StartRecordItem = Backbone.Model.extend({urlRoot: "/times/start/" });
RecordItem = Backbone.Model.extend({urlRoot: "/times/record/" });
ExtraMinutesItem = Backbone.Model.extend({urlRoot: "/times/record/" });

// Views 
var PanelRecordView = Backbone.View.extend({
	className: 'thumbnail thumb_act',
	
	template: _.template(
		'<div class = "caption">'+
            '<button id="act_stop" class ="btn btn-danger pull-right"> Stop </button>'+
            '<h3 id="actually_running" data-id = "<%= id %>" > <%= activity %> </h3>'+
            '<h4> <small> <%= time_start %> </small> </h4>'+
        '</div>'+
        '<img class = "image_act" src= <%= image %> ></img>'
        ),

	render: function(){
		var attributes = this.model.toJSON();
		this.$el.html(this.template(attributes));
	}
})

var ExtraMinutesView = Backbone.View.extend({
	tagName: 'li',
	className: function(){
		if(this.model.operation == "plus"){
			return "list-group-item list-group-item-success";
		}
		else{
			return "list-group-item list-group-item-danger";
		}
	},

	template: _.template(
		'<%= operation %> <%= minutes %> to <%= activity %>' +
		'<span class ="badge"> <%= minutes %> </span>'
	),

})


// Actions

// Stop
$("#act_panel").on("click", "#act_stop", function(){
	$.ajax({
		type: "PUT",
		url: "../stop/",
		success: function(){
			$("#act_panel").html('<img src="http://images.acgon.com/Uploadfile/Products/mp0010/mp0010.jpg">')
		}	
	})
});


// Start
$(".act_btn").on("click", function(){
	var act_id = $(this).attr("data-id");
	startRecordItem = new StartRecordItem({
		activity: act_id,
	});
	startRecordItem.save(null,{
			success: function(response){
				console.log(response);
				var data = response.toJSON();

				recordItem = new RecordItem({
					id: data.id,
				});
				recordItem.fetch({
					success: function(){
						panelRecordView = new PanelRecordView({
							model: recordItem
						});
						panelRecordView.render();
						$("#act_panel").html(panelRecordView.$el.html());
					}
				});
			}
		});
});


// Minutes Operations

$("#formAdd_send").on('click', function(){

});
