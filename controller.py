from flask import Flask, json, jsonify, redirect, url_for
from flask_cors import CORS
from room_service import RoomService
from book_service import BookService
from session_service import SessionService
import typing, json

app = Flask(__name__)
CORS(app)

curr_student_name = ""

@app.route("/")
def test():
  return( "Welcome to Hekman!" )

@app.route("/login")
def login() :
  session_service = SessionService()
  return session_service.log_in()
  return "Login Page"

@app.route("/logout")
def logout() :
  session_service = SessionService()
  return session_service.log_out()

@app.route("/reserve_room")
def reserve_room(room_id: str):
  room_service = RoomService()

  # this doesn't stop users from reserving the room multiple times
  reserved_room = room_service.reserve_room(room_id)
  return type(reserved_room)

@app.route("/show_rooms")
def rooms():
  room_service = RoomService()
  
  return(room_service.find_all())

@app.route("/show_books")
def books():
  book_service = BookService()
  
  return(book_service.find_all())

@app.route("/checkout_books")
def checkout_book(book_id: str):
  book_service = BookService()
  checked_out_room = book_service.checkout_book(book_id, curr_student_name)
  return checked_out_room

if __name__ == "__main__":
    app.run()