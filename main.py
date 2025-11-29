import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the basic python command that is being executed")

class animalsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class oddEvenRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            res = "odd" if int(num) % 2 else "even"
            self.write(f"This number {num} is {res}.")
        else:
            self.write(f"{num} is not a valid integer.")

class studentsRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(f"Welcome {student_name} the course you are viewing is {course_id}.")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        with open("list.txt", "r") as f:
            items = f.read().splitlines()
        self.write(json.dumps(items))
    def post(self):
        new_item = self.get_argument("item")
        with open("list.txt", "a") as f:
            f.write(f"{new_item}\n")
        self.write(json.dumps({"message": "Item added successfully"}))
if __name__ == "__main__":
    app = tornado.web.Application(
            [
                (r"/", basicRequestHandler),
                (r"/animals", animalsRequestHandler),
                (r"/odd-even", oddEvenRequestHandler),
                (r"/students/([a-z]+)/([0-9]+)", studentsRequestHandler),
                (r"/list", listRequestHandler)

            ]
        )
    port = 8882
    try:
        app.listen(port)
        print(f"Application is running on port {port}")
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        print(f"Error: {e}")
