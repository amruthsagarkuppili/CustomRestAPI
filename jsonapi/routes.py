######################################
#                                    #
# @author Amruth Sagar Kuppili       #
#                                    #
######################################
import base64

from flask import render_template, Blueprint, make_response
from jsonapi.actions.Sendrequest import Sendrequest
from flask import request, session


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__
)


@home_bp.route("/api/ping")
def ping():
    res = {"message": "ping"}
    return render_template('index.html',result=res)

@home_bp.route("/api/posts")
def posts():
    sendrequest = Sendrequest()
    res = {"message":"posts"}
    tags = request.args.get("tags")
    sortby = request.args.get("sortBy")
    direction = request.args.get("direction")
    if (tags is None):
        res["error"] = "Tags parameter is required"
        res["statuscode"] = 400
        return render_template('index.html', result=res)
    if (not(sortby is None) and (sortby not in ["id", "reads", "popularity", "likes"])):
        res["error"] = "sortBy parameter is invalid"
        res["statuscode"] = 400
        return render_template('index.html', result=res)
    if(not(direction is None) and (direction not in ["desc", "asc"])):
        res["error"] = "direction parameter is invalid"
        res["statuscode"] = 400
        return render_template('index.html', result=res)

    if sortby is None:
        sortby = "id"
    if direction is None:
        direction = "asc"
    # Check if cookie is present in session. If not present, hit the server else fetch the cookie
    if(session.get(tags+sortby+direction) == None):

        response, statuscode = sendrequest.hitLink(tags, sortby, direction)
        res["statuscode"] = statuscode

        # Storing in session cookie for faster retrieval. This doesn't hit the server'
        session[tags+sortby+direction] = response
    else:
        response = session.get(tags + sortby + direction)
    return make_response(render_template('index.html', result=res, response=response))