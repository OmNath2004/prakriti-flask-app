from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change in production

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # Collect form data
        form_data = request.form
        scored_questions = ['skin', 'body', 'hair', 'eyes', 'mindset', 'memory', 'emotions', 'diet', 'sleep', 'energy', 'weather', 'stress']
        vata_score = 0
        pitta_score = 0
        kapha_score = 0
        observations = {}
        total_answered = 0

        for q in scored_questions:
            answer = form_data.get(q)
            note = form_data.get(f'{q}_note', '')
            observations[q] = {'selection': answer, 'note': note}
            if answer in ['vata', 'pitta', 'kapha']:
                total_answered += 1
                if answer == 'vata':
                    vata_score += 1
                elif answer == 'pitta':
                    pitta_score += 1
                elif answer == 'kapha':
                    kapha_score += 1

        # Validation: Require at least some answers
        if total_answered < 3:
            flash('Please answer at least 3 questions for a meaningful analysis.', 'warning')
            return redirect(url_for('questionnaire'))

        # Determine dominant traits
        dominant_traits = []
        max_score = max(vata_score, pitta_score, kapha_score)
        if vata_score == max_score and vata_score > 0:
            dominant_traits.append('Vata')
        if pitta_score == max_score and pitta_score > 0:
            dominant_traits.append('Pitta')
        if kapha_score == max_score and kapha_score > 0:
            dominant_traits.append('Kapha')

        # Determine primary dosha
        if not dominant_traits:
            primary_dosha = 'Balanced (Insufficient data - try more answers)'
        elif len(dominant_traits) > 1:
            primary_dosha = 'Combination (' + '-'.join(dominant_traits) + ')'
        else:
            primary_dosha = dominant_traits[0]

        # Reflection
        reflection = form_data.get('reflection', '').strip()
        if not reflection:
            reflection = 'Please reflect on your results: How do these traits influence your daily life, health, and well-being? What steps can you take to maintain balance?'

        # Render with results
        return render_template('questionnaire.html',
                        stage='results',
                            observations=observations,
                            vata_score=vata_score,
                            pitta_score=pitta_score,
                            kapha_score=kapha_score,
                            total_answered=total_answered,
                            dominant_traits=dominant_traits,
                            primary_dosha=primary_dosha,
                            reflection=reflection)

    # GET: Show form
    return render_template('questionnaire.html', stage='form')

if __name__ == '__main__':
    app.run(debug=True)