$('#intro_next_btn').click(function() {
  $('#intro_expand_div').toggleClass('hidden');
  $('#intro_desc_div').toggleClass('hidden');

  $('#intro_begin_btn').click(function() {
    $(this).unbind('click');
    window.location.href = "/pamiexp/prac0";
  });

  $(this).unbind('click');
});

$('#prac0_begin_btn').click(function() {
  $('#prac0_instructions_div').toggleClass('hidden');

  setTimeout(function(){
      $('#prac0_probe_div').toggleClass('hidden');
      setTimeout(function(){
          $('#prac0_probe_div').toggleClass('hidden');

          setTimeout(function(){

            $('#prac0_response_div').toggleClass('hidden');

            function solution()
            {
              $('#prac0_0_btn').unbind('click');
              $('#prac0_1_btn').unbind('click');
              $('#prac0_2_btn').unbind('click');

              $('#prac0_0_btn').toggleClass('disabled');
              $('#prac0_1_btn').toggleClass('disabled');
              $('#prac0_2_btn').toggleClass('disabled');

              $('#prac0_answer_div').toggleClass('hidden');
              $('#prac0_exp0_btn').click(function() {
                $(this).unbind('click');
                window.location.href = "/pamiexp/exp0";
              });
            }

            $('#prac0_0_btn').click(function(){
              $('#prac0_0_btn').toggleClass('btn-info');
              $('#prac0_0_btn').toggleClass('btn-danger');

              solution();
            });

            $('#prac0_1_btn').click(function (){
              $('#prac0_1_btn').toggleClass('btn-info');
              $('#prac0_1_btn').toggleClass('btn-success');

              solution();
            });

            $('#prac0_2_btn').click(function (){
              $('#prac0_2_btn').toggleClass('btn-info');
              $('#prac0_2_btn').toggleClass('btn-danger');

              solution();
            });

          }, 500);
      }, 200);
  }, 500);

  $(this).unbind('click');
});

$('#prac1_begin_btn').click(function() {
  $('#prac1_instructions_div').toggleClass('hidden');

  setTimeout(function(){
      $('#prac1_probe_div').toggleClass('hidden');
      setTimeout(function(){
          $('#prac1_probe_div').toggleClass('hidden');

          setTimeout(function(){

            $('#prac1_response_div').toggleClass('hidden');

            function solution()
            {
              $('#prac1_0_btn').toggleClass('btn-info');
              $('#prac1_0_btn').toggleClass('btn-success');
              $('#prac1_0_btn').unbind('click');
              $('#prac1_1_btn').unbind('click');

              $('#prac1_0_btn').toggleClass('disabled');
              $('#prac1_1_btn').toggleClass('disabled');

              $('#prac1_answer_div').toggleClass('hidden');
              $('#prac1_exp0_btn').click(function() {
                $(this).unbind('click');
                window.location.href = "/pamiexp/exp1";
              });
            }

            $('#prac1_0_btn').click(function(){
              solution();
            });

            $('#prac1_1_btn').click(function (){
              $('#prac1_1_btn').toggleClass('btn-info');
              $('#prac1_1_btn').toggleClass('btn-danger');

              solution();
            });
          }, 500);
      }, 200);
  }, 500);

  $(this).unbind('click');
});

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

function getexp(ex) {
  var exp = getCookie(ex);
  exp = $.parseHTML(exp)[0].wholeText;
  exp = exp.split("\"")[1].split("\\054");
  exp = exp.map(function(x) {
    return parseInt(x);
  });
  return exp;
}

function exp0next(id) {
  setTimeout(function(){
    $('#exp0_probe_' + id + '_div').toggleClass('hidden');
    setTimeout(function(){
      $('#exp0_probe_' + id + '_div').toggleClass('hidden');
      setTimeout(function(){
        $('#exp0_response_' + id + '_div').toggleClass('hidden');

        var exp0 = getexp('exp0');
        var index = 0;
        for (i = 0; i < exp0.length; i++) {
          if (exp0[i] === id) {
            index = i;
            break;
          }
        }

        var exp0res = getexp('exp0res');

        function choose(btn) {
          $('#exp0_' + id + '_0_btn').unbind('click');
          $('#exp0_' + id + '_1_btn').unbind('click');
          $('#exp0_' + id + '_2_btn').unbind('click');

          if ($('#exp0_' + id + '_' + btn + '_input')[0].value === 'True') {
            exp0res[index] = 1;
          }else {
            exp0res[index] = 0;
          }
          var tmp = exp0res.map(function(x) {
            return x.toString();
          })

          tmp = exp0res.join("\\054");

          document.cookie = 'exp0res="'+tmp+'";path=/;expires=Session;';

          $('#exp0_response_' + id + '_div').toggleClass('hidden');

          if (index+1 < exp0.length) {
            exp0next(exp0[index+1]);
          } else {
            window.location.href = "/pamiexp/prac1";
          }
        }

        $('#exp0_' + id + '_0_btn').click(function (){
          choose('0');
        });

        $('#exp0_' + id + '_1_btn').click(function (){
          choose('1');
        });

        $('#exp0_' + id + '_2_btn').click(function (){
          choose('2');
        });


      },500);

    }, 50);

  }, 500);
}

function exp1next(id) {
  setTimeout(function(){
    $('#exp1_probe_' + id + '_div').toggleClass('hidden');
    setTimeout(function(){
      $('#exp1_probe_' + id + '_div').toggleClass('hidden');
      setTimeout(function(){
        $('#exp1_response_' + id + '_div').toggleClass('hidden');

        var exp1 = getexp('exp1');
        var index = 0;
        for (i = 0; i < exp1.length; i++) {
          if (exp1[i] === id) {
            index = i;
            break;
          }
        }

        var exp1res = getexp('exp1res');

        function choose(btn) {
          $('#exp1_' + id + '_0_btn').unbind('click');
          $('#exp1_' + id + '_1_btn').unbind('click');

          if ($('#exp1_' + id + '_' + btn + '_input')[0].value === 'True') {
            exp1res[index/2] = 1;
          }else {
            exp1res[index/2] = 0;
          }
          var tmp = exp1res.map(function(x) {
            return x.toString();
          })

          tmp = exp1res.join("\\054");

          document.cookie = 'exp1res="'+tmp+'";path=/;expires=Session;';

          $('#exp1_response_' + id + '_div').toggleClass('hidden');

          if (index+2 < exp1.length) {
            exp1next(exp1[index+2]);
          } else {
            window.location.href = "/pamiexp/results";
          }
        }

        $('#exp1_' + id + '_0_btn').click(function (){
          choose('0');
        });

        $('#exp1_' + id + '_1_btn').click(function (){
          choose('1');
        });

      },500);

    }, 50);

  }, 500);
}


$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();

    var exp0 = getexp('exp0');
    var exp0res = getexp('exp0res');
    var exp1 = getexp('exp1');
    var exp1res = getexp('exp1res');

    exp0next(exp0[0]);
    exp1next(exp1[0]);

});
