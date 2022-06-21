from flask import Flask, json, jsonify
from flask_cors import CORS
from room_service import RoomService
from book_service import BookService
from session_service import SessionService
import typing

app = Flask(__name__)
CORS(app)

curr_student_name = ""

@app.route("/")
def test():
  return "Welcome to Hekman!"

def login() :
  session_service = SessionService()
  session_service.log_in()

def logout() :
  session_service = SessionService()
  session_service.log_out()

def reserve_room(room_id: str):
  room_service = RoomService()

  # this doesn't stop users from reserving the room multiple times
  reserved_room = room_service.reserve_room(room_id)
  return reserved_room

def rooms():
  room_service = RoomService()
  print(room_service.find_all())

def books():
  book_service = BookService()
  print(book_service.find_all())

def checkout_book(book_id: str):
  book_service = BookService()
  checked_out_room = book_service.checkout_book(book_id, curr_student_name)
  return checked_out_room

if __name__ == "__main__":
    app.run()