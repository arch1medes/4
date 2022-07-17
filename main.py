from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_page():
    candidates:list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:mn>")
def candidate_page(mn):
    candidate:list[dict] = get_candidate(mn)
    if not candidate:
        return "not found"
    return  render_template('.cardhtml', candidates=candidate)

@app.route("/search/candidate<int:mk>")
def candidate_search(mn):
    candidate:list[dict] = get_candidates_by_name(mk)
    if not candidate:
        return "not found"
    return  render_template('single.html', candidates=candidate)

@app.route("/skill/candidate<int:mp>")
def candidate_skill(mp):
    candidate:list[dict] = get_candidates_by_skill(mk)
    if not candidate:
        return "not found"
    return  render_template('sing.html', candidates=candidate)






app.run()