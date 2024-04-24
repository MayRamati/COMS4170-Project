$(function() {
    $(".draggable").draggable({
        helper: "clone",
        revert: "invalid", // Revert if dropped incorrectly
        opacity: 0.7       // Make the drag helper slightly transparent
    });

    $(".droppable").droppable({
        accept: ".draggable",
        tolerance: "intersect", // Requires the draggable to intersect the droppable
        drop: function(event, ui) {
            var draggableName = ui.draggable.data('name').trim();
            var droppableName = $(this).data('name').trim();
            if (draggableName === droppableName) {
                // Correct match
                ui.draggable.css('border', '3px solid #50C878'); // Set the draggable's border color on correct drop
                ui.draggable.draggable('disable'); // Disable further dragging
                $(this).droppable('disable'); // Disable the droppable area
                ui.draggable.position({ // Position the draggable centered to the droppable
                    my: "center",
                    at: "center",
                    of: $(this),
                    using: function(pos) {
                        $(this).animate(pos, 200, "linear"); // Smooth animation to center
                    }
                });
            } else {
                // If not a match, revert
                ui.draggable.draggable('option', 'revert', true);
            }
        }
    });

    $("#submit-quiz").on('click', function() {
        var correctMatches = 0;
        $(".draggable").each(function() {
            if ($(this).css('border-color') === 'rgb(80, 200, 120)') { // Check if the border color is green (#50C878)
                correctMatches += 1;
            }
        });

        $.ajax({
            url: '/quiz/1/score', // This needs to be dynamically set or correctly routed
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
