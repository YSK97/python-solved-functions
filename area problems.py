{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3907885e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length2\n",
      "height4\n",
      "area 4.0\n"
     ]
    }
   ],
   "source": [
    "#area problems\n",
    "b=int(input(\"length\"))\n",
    "h=int(input('height'))\n",
    "area=b*h/2\n",
    "print(\"area\",area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "44cb58d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number5\n",
      "enter a number6\n",
      "enter a number7\n",
      "area of triangle is 93.71\n"
     ]
    }
   ],
   "source": [
    "s1=int(input('enter a number'))\n",
    "s2=int(input('enter a number'))\n",
    "s3=int(input('enter a number'))\n",
    "s=s1+s2+s3/2\n",
    "area=(s*(s-s1)*(s-s2)*(s-s3))**0.5\n",
    "print(\"area of triangle is %0.2f\"%area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d545422",
   "metadata": {},
   "outputs": [],
   "source": [
    "s=int(input(\"sides\"))\n",
    "l=float(input(\"length\"))\n",
    "area=s*(l**2)/(4*1)(3.141/s)\n",
    "print(\"area of polygon:\",area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "789a3980",
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
