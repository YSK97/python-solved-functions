{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ef364d3f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number3\n",
      "6.0\n"
     ]
    }
   ],
   "source": [
    "#n*(n+1)/2\n",
    "n=int(input(\"enter a number\"))\n",
    "s=(n*(n+1))/2\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bdf94234",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number10\n",
      "enter a number20\n",
      "30 -10 200 0.5 10 100000000000000000000\n"
     ]
    }
   ],
   "source": [
    "#Arithmetic\n",
    "a=int(input(\"enter a number\"))\n",
    "b=int(input(\"enter a number\"))\n",
    "c=a+b\n",
    "d=a-b\n",
    "p=a*b\n",
    "q=a/b\n",
    "r=a%b\n",
    "re=a**b\n",
    "print(c,d,p,q,r,re)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c3d3dc97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "distance in feet:100\n",
      "distance in inc is 1200 inc.\n",
      "distance in yar is 33.33 yar.\n",
      "distance in mil is 0.02 mil.\n"
     ]
    }
   ],
   "source": [
    "#Distance units\n",
    "ft=int(input(\"distance in feet:\"))\n",
    "inc=ft*12\n",
    "yar=ft/3.0\n",
    "mil=ft/5280\n",
    "print(\"distance in inc is %i inc.\" % inc)\n",
    "print(\"distance in yar is %.2f yar.\" % yar)\n",
    "print(\"distance in mil is %.2f mil.\" % mil)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "35335740",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "radius of circle:3\n",
      "volume of sphere:6\n",
      "area of circle = 28.269\n",
      "volume of sphere = 90363.14315643598\n"
     ]
    }
   ],
   "source": [
    "#Area and volume\n",
    "a=float(input(\"radius of circle:\"))\n",
    "b=float(input(\"volume of sphere:\"))\n",
    "r=3.141*r*r\n",
    "v=4/3*a*r**3\n",
    "print(\"area of circle =\",r)\n",
    "print(\"volume of sphere =\",v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a14ab21f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "height of cylinder:3\n",
      "radius of cylinder:6\n",
      "volume: 339.42857142857144\n",
      "area: 339.42857142857144\n"
     ]
    }
   ],
   "source": [
    "#Volume of cylinder\n",
    "h=float(input(\"height of cylinder:\"))\n",
    "r=float(input(\"radius of cylinder:\"))\n",
    "pi=22/7\n",
    "v=pi*r*r*h\n",
    "a=((2*pi*r)*h)+((pi*r**2)*2)\n",
    "print(\"volume:\",v)\n",
    "print(\"area:\",a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "525c8bf9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
