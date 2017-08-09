<script>
	$(function(){
	    $('#sidebar').hover(
	        function() {
	            $(#sidebar2').fadeIn();
	        },
	        function() {
	            $('#sidebar2').fadeOut();
	        }
	    );

	    $('#sidebar2').hover(
	        function() {
	            $(this).stop(true, true);
	        },
	        function() {
	            $(this).stop(true, true).delay(50).fadeOut();
	        }
	});
</script>