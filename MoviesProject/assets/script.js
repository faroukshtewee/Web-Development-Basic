document.querySelectorAll('.star-rating-create input').forEach(input => {
    input.addEventListener('change', function() {
        const stars = this.value;
        document.querySelectorAll('.star-rating-create label').forEach(label => {
            label.style.color = (label.htmlFor <= stars) ? 'gold' : 'lightgray';
        });
    });
});
