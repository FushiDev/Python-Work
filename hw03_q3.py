# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:39:23 2021

@author: Dylan
"""

#Homework 3
import turtle
import images
t = turtle.Turtle()
turtle.speed(10)
screen = turtle.Screen()
screen.colormode(255)
screen.setup(450,450)



def draw_pixel(x,y,color,pixel_size):
  turtle.pu()
  turtle.setpos(x,y) #moves turtle to start point
  turtle.pd
  turtle.fillcolor(color)
  turtle.begin_fill()
  for _ in range(4):
    turtle.forward(pixel_size)
    turtle.right(90)
  turtle.end_fill()

def draw_image(image):
  size = 450/len(image)
  x = -225
  y = 225
  for i in range(len(image)):
    for l in range(len(image)):
      color = image[i][l]
      new = grayscale_conversion(color)
      draw_pixel(x,y,new,size)
      x += size
    x = -225
    y -= size

def grayscale_conversion(matrix):
  color = 0 
  for i in matrix:
    color += i
  color = round(color/3)
  color = [color,color,color]
  return color


def main():
  choice = input("What image to draw? (1/2/3/4) ")
  if choice == '1':
    draw_image(images.img1)
  if choice == '2':
    draw_image(images.img2)
  if choice == '3':
    draw_image(images.img3)
  if choice == '4':
    draw_image(images.img4)

if __name__ == '__main__':
  main()
  
turtle.done()
turtle.bye()