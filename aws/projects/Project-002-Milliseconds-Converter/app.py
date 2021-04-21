from flask import Flask, render_template,request

app = Flask(__name__)

def converter(miliseconds):
    if miliseconds < 1000:
        return miliseconds
    else:
        seconds, miliseconds = divmod(miliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return [hours, minutes, seconds]

def calculated_time(miliseconds):
    time = ["hour/s", "minute/s", "second/s"]
    calculated = converter(miliseconds)
    if type(calculated) == int:
        result = f"just {calculated} millisecond/s"
    else:
        result = " ".join([f"{calculated[i]} {time[i]}" for i in range(3) if calculated[i] != 0])
    return result

@app.route("/", methods=["POST","GET"])
def main(dev_name="Mehmet"):
    if request.method == "POST":
        post_value = request.form["number"].strip()
        if not post_value.isdecimal():
            return render_template("index.html", not_valid = True, developer_name = dev_name)
        number = int(post_value)
        if number <= 0:
            return render_template("index.html", not_valid = True, developer_name = dev_name)
        else:
            return render_template("result.html", result = calculated_time(number),
                                    developer_name = dev_name, miliseconds = number)
    
    else:
        return render_template("index.html", not_valid = False, developer_name = dev_name)





if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)