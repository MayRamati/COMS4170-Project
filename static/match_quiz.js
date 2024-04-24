$(function() {
    // Initialize draggable elements
    $(".draggable").draggable({
        helper: "clone",
        revert: "invalid",
        start: function(event, ui) {
            $(ui.helper).css("opacity", "0.5");  // Reduce opacity of the drag helper
        }
    });

    // Initialize droppable elements
    $(".droppable").droppable({
        accept: ".draggable",
        tolerance: "touch",  // Adjusted to 'touch' for better drop detection
        drop: function(event, ui) {
            let draggableName = ui.draggable.data('name').trim();
            let droppableName = $(this).data('name').trim();

            if (draggableName === droppableName) {
                // Correct match
                $(this).find('img').css('border', '3px solid green');
                ui.draggable.draggable('disable');
                $(this).droppable('disable');
                // Ensure the draggable snaps to center without being moved again
                ui.draggable.position({
                    my: "center",
                    at: "center",
                    of: $(this),
                    using: function(pos) {
                        $(this).animate(pos, 200, "linear");
                    }
                });
            } else {
                ui.draggable.draggable('option', 'revert', true);
            }
        }
    });

    // Function to handle the quiz submission
    $("#submit-quiz").on('click', function() {
        var correctMatches = 0;
        $(".droppable").each(function() {
            if ($(this).find('img').css('border-color') === 'rgb(0, 128, 0)') { // Checking if border is green
                correctMatches += 1;
            }
        });

        // Adjusted to potentially correct endpoint and handle errors
        $.ajax({
            url: '/quiz/1/score', // Simplified for demonstration; adjust as necessary
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({score: correctMatches}),
            success: function(response) {
                window.location.href = "/result"; // Redirect to the results page
            },
            error: function(xhr, status, error) {
                alert("Failed to submit score. Please try again.");
            }
        });
    });
});
