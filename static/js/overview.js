/* Models */
DayModel = Backbone.Model.extend({
});

WeekModel = Backbone.Model.extend({
});

/* Collections */
DayCollection = Backbone.Collection.extend({
	model: DayModel,
	url: '/times/api/day_list'
})

WeekCollection = Backbone.Collection.extend({
	model: WeekModel,
	url: '/times/api/week_list'
})

/* Views */
DayView = Backbone.View.extend({
	tagName: 'tr',
	render: function(){
		this.$el.html('<td>'+this.model.get('date')+'</td>'+
			'<td>'+this.model.get('comments')+'</td>'+'<td>'+this.model.get('minutes')+'</td>'+
			'<td>'+'<img class="trophy_small" src="'+this.model.get('trophy')+'"</img>'+'</td>');
	}
})

WeekView = Backbone.View.extend({
	tagName: 'tr',
	render: function(){
		this.$el.html('<td>'+this.model.get('date')+'</td>'+
			'<td>'+this.model.get('comments')+'</td>'+'<td>'+this.model.get('hours')+'</td>'+
			'<td>'+'<img class="trophy_small" src="'+this.model.get('trophy')+'"</img>'+'</td>');
	}
})

CollectionDayView = Backbone.View.extend({
	tagName: 'table',
	className: 'table',

	initialize: function(){
		this.collection.on('reset', this.addAll, this);
	},

	addAll: function(){
		this.collection.forEach(this.addOne, this);		
	},

	addOne: function(dayItem){
		var dayView = new DayView({model:dayItem});
		dayView.render()
		this.$el.append(dayView.el);
	},

	render: function(){
		this.$el.append('<tr> <th> Date </th> <th> Comment </th> <th> Time </th> <th> Icon </th> </tr>');
		this.addAll();
	}
});

CollectionWeekView = Backbone.View.extend({
	tagName: 'table',
	className: 'table',

	initialize: function(){
		this.collection.on('reset', this.addAll, this);
	},

	addAll: function(){
		this.collection.forEach(this.addOne, this);
	},

	addOne: function(weekItem){
		var weekView = new WeekView({model:weekItem});
		weekView.render();
		this.$el.append(weekView.el)
	},

	render: function(){
		this.$el.append('<tr> <th> Week Number </th> <th> Comment </th> <th> Time </th> <th> Icon </th> </tr>');
		this.addAll();
	}
})

/* Router-App */
var OverviewApp = new (Backbone.Router.extend({
	routes : {
			"times/overview": "times_day", 
	        "times/overview/weeks": "times_week"
	      },

	initialize: function(){
		this.dayCollection = new DayCollection({});
		this.weekCollection = new WeekCollection({});

		this.dayTableView = new CollectionDayView({collection: this.dayCollection});
		this.weekTableView = new CollectionWeekView({collection: this.weekCollection});

		this.dayCollection.fetch({
			success: function(){
				this.dayTableView.render(this.dayTableView);
				$("#times_day").html(this.dayTableView.el);
			}.bind(this)
		});
	},

	start: function(){
		Backbone.history.start({pushState: true});
		console.log("llego function start");
	},

	times_day: function(){
		$("#times_day").removeClass("hidden");
		$("#times_week").addClass("hidden");
	},

	times_week: function(){
		console.log("llego times_week")
		$("#times_day").addClass("hidden");
		$("#subtl-header").text("times/week");
	
		if ($("#times_week").hasClass("hidden")){
			$("#times_week").removeClass("hidden");
		}
		else{
		this.weekCollection.fetch({
			success: function(){
				this.weekTableView.render();
				$("#times_week").html(this.weekTableView.el);
			}.bind(this)
		});
		}
	},
}));


/* Actions */
$(document).ready(function(){ 
	OverviewApp.start() 
});

$("#activate_timesweek").on('click', function(){
	OverviewApp.navigate("times/overview/weeks", {trigger: true});
});

$("#activate_timesday").on('click', function(){
	OverviewApp.navigate("times/overview", {trigger: true});
});					

		