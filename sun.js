$(document).ready(function(){
	var id = 1;
	var idd=0;
	//unique identifier to questions
	var questionTypes = 1;
	//unique identifier to answers
	var answer = 1;
	var maxField = 50;
	var x = 1;
	//dynamically adds a new question
	$('#add').click(function(){
		//$("#question-"+id+"").disable();
		$("#select-"+id+"").hide();
		$("#inputgroup-"+id+"").append(
			'<button type = "button"   id="edit-'+id+'" style = "color:brown">Edit</button>'
		);

		$("#edit-"+id+"").click(function(){
			$(this).hide();
			$("#select-"+id+"").show();
		});

		if(x < maxField){
		x++;//Increment field counter
		id++;
		questionTypes++;

		$('#dynamic_field').append(

			'<div name="qn-'+id+'" id="qn-'+id+'" class="que">' +
				'<div class="form-group">'+
					'<label>'+id+'.</label>'+
				'</div>'+
				'<div class="input-group mb-3" id = "inputgroup-'+id+'">'+
					'<textarea class="form-control" name="question-'+id+'" id="question'+id+'"placeholder="Question here..." style="color:blue;"></textarea>'+
					'<div id = "select-'+id+'">'+
					'<div class="input-group-append">'+
						'<span  id="questionTypes-'+id+'" name="questionTypes-'+id+'" class="input-group-text">'+
							'<select name="slct" class="dan'+id+' form-control" id="'+id+'">'+
							'<option selected = "selected">Select answer type</option>'+
							'<option value = "text">Short answer</option>'+
		          '<option value = "paragraph">Paragraph</option>'+
							'<option value = "single">Single Choice</option>'+
							'<option value = "multiple">Multiple Choices</option>'+
		          '<option value = "file">File upload</option>'+
		          '<option value = "dropdown">Dropdown</option>'+
		          '<option value = "linear">Linear scale</option>'+
		          '<option value = "mulgrid">Multiple Choice grid</option>'+
		          '<option value = "checkgrid">Check box grid</option>'+
		          '<option value = "date">Date</option>'+
		          '<option value = "time">Time</option>'+
							'</select>'+
						'</span>'+
					'</div>'+
					'<div class="input-group-append">'+
						'<span class="input-group-text">'+
							'<b><button id="'+id+'" name="remove" type="submit" class="remove btn-danger">X</button></b>'+
						'</span>'+
					'</div>'+
					'</div>'+
				'</div>'+
				'<div id="answerTypes-'+id+'" name = "answerTypes-'+id+'" class="form-group">'+
				'</div>'+
			'</div>'

			);
		//adds the select options from another file
		$("#"+id+"").load('questionTypes1.htm');
		return false;
	}
	});



	//removes the question that was added dynamically
	$(document).on('click','.remove',function(){
		var button_id = $(this).attr("id");
		$("#qn-"+button_id+"").remove();
		x--; //Decrement field counter
		id--; //Decrement question number

	});

	//changes answer format according to the question type selected
	$('form').on('change','select[name="slct"]',function() {
	    //CHANGE EVENT CODE HERE
	    var slct_id = $(this).attr("id");
		var optionSelected = $(this).find("option:selected");
		var valueSelected  = optionSelected.val();
		var textSelected   = optionSelected.text();

		if (valueSelected == 'text') {

			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<input type = "text" class="form-control" name="answer-'+slct_id+'" id="answer-'+slct_id+'"  placeholder="Answer here..."></input>'

			);

		}
		if (valueSelected == 'paragraph') {

			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<textarea  class="form-control" name="answer-'+slct_id+'" id="answer-'+slct_id+'"  placeholder="Answer here..."></textarea>'

			);

		}
		if (valueSelected == 'single') {
			var cid = 1;
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
		//	$("#answerTypes-"+slct_id+"").append(

				//'<div name="answer-'+slct_id+'" id="answer-'+slct_id+'">'+
				$("#answerTypes-"+slct_id+"").append(

					'<div name="answer-'+slct_id+'" id="answer-'+slct_id+'">'+
					'<input type = "radio" name = "roption-'+cid+'" id ="roption-'+cid+'"/>&nbsp&nbsp'+
					'<input type = "text" placeholder = "Option" name = "qoption-'+cid+'" id ="qoption-'+cid+'"/>'+
					'<button type="button" class = "rrbutton">+</button>'+
					'</div>'

					);

					$(".rrbutton").click(function(){
						cid++;
						//var radi = '<div id = "rad"><input type = "radio"/>&nbsp&nbsp<input type = "text" placeholder = "Option"/><button type="button" class = "rrrbutton">X</button></div>';
						//window.alert("Hey there");
						$("#answer-"+slct_id+"").append(
							'<div name="answer-'+slct_id+'" id="answer-'+slct_id+'">'+
							'<input type = "radio" name = "roption-'+cid+'" id ="roption-'+cid+'"/>&nbsp&nbsp'+
							'<input type = "text" placeholder = "Option" name = "qoption-'+cid+'" id ="qoption-'+cid+'"/>'+
							'<button type="button" class = "rrrbutton">X</button>'+
							'</div>'
						);
					});

					$("#answer-"+slct_id+"").on('click', '.rrrbutton', function(e){
							e.preventDefault();
							$(this).parent('div').remove(); //Remove field html

							cid--;



				//'</div>'
			});

		}
		if (valueSelected == 'multiple') {

			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<div name="answer-'+slct_id+'" id="answer-'+slct_id+'" class="optionn">'+
				'<input type = "checkbox"/>&nbsp&nbsp'+
				'<input type = "text" id="optionn'+idd+'" placeholder = "Option"/>'+
				'<button type="button" class = "rrbutton">+</button>'+
				'</div>'

				);

				$(".rrbutton").click(function(){
					idd++;
					//var radi = '<div id = "rad"><input type = "radio"/>&nbsp&nbsp<input type = "text" placeholder = "Option"/><button type="button" class = "rrrbutton">X</button></div>';
					//window.alert("Hey there");
					$("#answer-"+slct_id+"").append(
						'<div name="answer-'+slct_id+'" id="answer-'+slct_id+'" class="optionn">'+
						'<input type = "checkbox"/>&nbsp&nbsp'+
						'<input type = "text" id="optionn'+idd+'" placeholder = "Option"/>'+
						'<button type="button" class = "rrrbutton">X</button>'+
						'</div>'
					);
				});

				$("#answer-"+slct_id+"").on('click', '.rrrbutton', function(e){
						e.preventDefault();
						$(this).parent('div').remove(); //Remove field html




			//'</div>'
		});


		}

		if (valueSelected == 'file') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<input type = "file" name="answer-'+slct_id+'" id="answer-'+slct_id+'"></input>'
			);
		}

		if (valueSelected == 'dropdown') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append();
		}

		if (valueSelected == 'linear') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<input type = "range" min = "0" max = "10" step = "1" name="answer-'+slct_id+'" id="answer-'+slct_id+'"/>'
			);
		}

		if (valueSelected == 'mulgrid') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append();
		}

		if (valueSelected == 'checkgrid') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append();
		}

		if (valueSelected == 'date') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<input type = "date" name="answer-'+slct_id+'" id="answer-'+slct_id+'"></input>'
			);
		}

		if (valueSelected == 'time') {
			//remove first whats in the answer section before appending a new type
			$("#answer-"+slct_id+"").remove();
			$("#answerTypes-"+slct_id+"").append(

				'<input type = "time" name="answer-'+slct_id+'" id="answer-'+slct_id+'"></input>'
			);
		}
	});




	//auto resizing the textareas
	function autosize(textarea) {
	    $(textarea).height(1); // temporarily shrink textarea so that scrollHeight returns content height when content does not fill textarea
	    $(textarea).height($(textarea).prop("scrollHeight"));
	}

	$(document).ready(function () {
	    $(document).on("input", "textarea", function() {
	        autosize(this);
	    });
	    $("textarea").each(function () {
	        autosize(this);
	    });
	});

	//submit the form input to the API
	$('#submit').click(function(){
		$.ajax({
			url:"name.php",
			method:"POST",
			data:$('#survey').serialize(),
			success:function(data){
				alert(data);
				$('#survey')[0].reset();
			}
		});
	});




// here is arnold's code
$(".buttonwe").click(function(){
 jso={};
 d={};
survey_details = {}
var title = $("#title").val();
var description = $("#description").val();
alert(description);
survey_details ["title"] = title;
survey_details ["userName"] = "";
d = survey_details;
jso['survey']=d;
wep={};
wp=[];
$(".que").each(function(index,value){
 item = {};
var indexx=index+1;

var type_of_question = $(".dan"+indexx).find(":selected").val();

var type = $("#question"+indexx).val();

    if(type_of_question=="multiple"){
    	// alert("here we go")
    	// json = [];  
    	// $(".optionn").each(function(ind,value){
    	//   options={}; 
    	//   var optionselect = $("#optionn"+ind).val();
     //       options["option"] = optionselect;
     //       json.push(options);

    	// });
     //   item["question_number"] = indexx;
     //   item ["question"] = type;
     //   item ["question_type"] = type_of_question;
     //   item["options"]=json;

     //   jsonObj.push(item);
       	
   }else{
 	   item["questionID"] = indexx;
       item ["question"] = type;
       item ["questionType"] = type_of_question;
       item["options"] ="null";
       		wep=item;
       		wp.push(wep);   		
	        }
});

 jso['surveyQuestion']=wp;
     $.ajax
	    ({
	        type: "GET",
	        dataType : 'json',
	        async: false,
	        url: 'save_json.php',
	        data: { data: JSON.stringify(jso) },
	        success: function () {alert("Thanks!"); },
	        failure: function() {alert("Error!");}
	    });      
	

	});



});
