$(document).ready(function() {
	$('#likes').click(function() {
		var catid;
		catid = $(this).attr('data-catid');
		$.get('/rango/like_category/',{category_id: catid},function(data) {
			$('#like_count').html(data);
			$('#likes').hide();
		});
	});
	$('#top_cats').load('/rango/suggest_category/?suggestion=*');
	$('#suggestion').keyup(function() {
		var query;
		query = $(this).val();
		$.get('/rango/suggest_category/',{suggestion: query},function(data) {
			$('#cats').html(data);
		});
	});
	$('.rango_add').click(function() {
		var name,p_title,p_url;
		name = $(this).attr('data-catname');
		p_title = $(this).attr('data-title');
		p_url = $(this).attr('data-url');
		num = $(this).attr('data-id');
		e = $(this);
		$.get('/rango/auto_add_page/',{category_name: name,title: p_title, url:p_url}, function(data){
			$('#page_list').html(data);
			e.hide();
		});
	});
});
