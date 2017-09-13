$('.papers-abs-btns').click(function() {
    $('#'+this.id).toggleClass('glyphicon-collapse-down');
    $('#'+this.id).toggleClass('glyphicon-collapse-up');
    key = this.id.substr(0,this.id.length-8);
    $('#'+key+'_abs_div').toggleClass('hidden');
    $('#'+key+'_abs_div').toggleClass('show');
})
