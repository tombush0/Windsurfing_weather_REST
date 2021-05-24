from app import app, config
from app.api.stormglass import StormGlassAPI
from app.Parsing.form_parser import parse_form
from app.Requests.forms import UserInputForm
from app.Parsing.summary_parser import get_summary
from flask import render_template, redirect, url_for, session, request


@app.route("/", methods=["GET", "POST"])
def index():
    form = UserInputForm()
    if form.validate_on_submit():
        session["form"] = request.form
        return redirect(url_for("results"))
    return render_template("index.html", form=form)


@app.route("/results")
def results():
    city = session["form"]["city"]
    lat, lng, date_from, date_to = parse_form(session["form"])

    storm_glass_api = StormGlassAPI(config.storm_glass_key)
    storm_glass_results = storm_glass_api.request(lat, lng, date_from, date_to)

    storm_glass_summary = get_summary(storm_glass_results)

    date_from = date_from.strftime("%d/%m/%Y")
    date_to = date_to.strftime("%d/%m/%Y")

    return render_template("results.html",
                           city=city,
                           date_from=date_from,
                           date_to=date_to,
                           storm_glass_summary=storm_glass_summary)