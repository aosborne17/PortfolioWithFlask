// Note that in order for this script to work we need to load jquery into our HTML!!

$(function() {
    // here we are binding the id of a html element
    // Note that the "#" sign means jquery will look for an element id = to what is specified
    $('#sendBtn').bind('click', function() {
    // When the button is clicked, it will run a function specified in our python files
      $.getJSON('/run',
          function(data) {
        //do nothing
      });
      return false;
    });
  });