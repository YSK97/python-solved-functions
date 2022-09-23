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
   "execution_count": null,
   "id": "35335740",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Area and volume\n",
    "a=float(input(\"radius of circle:\"))\n",
    "r=3\n",
    "aa=3.141*r*r\n",
    "v=4/3*22/7*r**3\n",
    "print(\"area of circle =\",r)\n",
    "print(\"volume of sphere =\",v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a14ab21f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "height of cylinder:4\n",
      "radius of cylinder:6\n",
      "volume: 452.57142857142856\n",
      "area: 377.1428571428571\n"
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
   "source": [
    "r=float(input(\"radius of circle:\"))\n",
    "area=3.1416*r\n",
    "print(\"radius:\",r)\n",
    "print(\"area=\",area)\n",
    "ra=float(input(\"radius of sphere:\"))\n",
    "pi=22/7\n",
    "sur_area=4*pi*ra**2\n",
    "v=4/3*pi*ra**3\n",
    "print(\"sur_area:\",sur_area)\n",
    "print(\"volume:\",volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45396e85",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07936fbd",
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
