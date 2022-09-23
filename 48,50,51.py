{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7f2b0706",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter range of magnitude:8\n",
      "great\n"
     ]
    }
   ],
   "source": [
    "#50 Richter scale \n",
    "magnitude=float(input(\"enter range of magnitude:\"))\n",
    "if(magnitude<2.0):\n",
    "    print(\"micro\")\n",
    "elif(magnitude>=2.0 and magnitude<3.0):\n",
    "    print(\"very minor\")\n",
    "elif(magnitude>=3.0 and magnitude<4.0):\n",
    "    print(\"minor\")    \n",
    "elif(magnitude>=4.0 and magnitude<5.0):\n",
    "    print(\"light\")\n",
    "elif(magnitude>=5.0 and magnitude<6.0):\n",
    "    print(\"moderate\")\n",
    "elif(magnitude>=6.0 and magnitude<7.0):\n",
    "    print(\"strong\")\n",
    "elif(magnitude>=7.0 and magnitude<8.0):\n",
    "    print(\"majorr\") \n",
    "elif(magnitude>=8.0 and magnitude<10.0):\n",
    "    print(\"great\")\n",
    "elif(magnitude>=10.0):\n",
    "    print(\"meteoric\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2a68897b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input birthday: 4\n",
      "Input month of birth (e.g. march, july etc): january\n",
      "Your Astrological sign is : Capricorn\n"
     ]
    }
   ],
   "source": [
    "#48 birthdate astrological sign\n",
    "day = int(input(\"Input birthday: \"))\n",
    "month = input(\"Input month of birth (e.g. march, july etc): \")\n",
    "if month == 'december':\n",
    "\tastro_sign = 'Sagittarius' if (day < 22) else 'capricorn\n",
    "elif month == 'january':\n",
    "\tastro_sign = 'Capricorn' if (day < 20) else 'aquarius'\n",
    "elif month == 'february':\n",
    "\tastro_sign = 'Aquarius' if (day < 19) else 'pisces'\n",
    "elif month == 'march':\n",
    "\tastro_sign = 'Pisces' if (day < 21) else 'aries'\n",
    "elif month == 'april':\n",
    "\tastro_sign = 'Aries' if (day < 20) else 'taurus'\n",
    "elif month == 'may':\n",
    "\tastro_sign = 'Taurus' if (day < 21) else 'gemini'\n",
    "elif month == 'june':\n",
    "\tastro_sign = 'Gemini' if (day < 21) else 'cancer'\n",
    "elif month == 'july':\n",
    "\tastro_sign = 'Cancer' if (day < 23) else 'leo'\n",
    "elif month == 'august':\n",
    "\tastro_sign = 'Leo' if (day < 23) else 'virgo'\n",
    "elif month == 'september':\n",
    "\tastro_sign = 'Virgo' if (day < 23) else 'libra'\n",
    "elif month == 'october':\n",
    "\tastro_sign = 'Libra' if (day < 23) else 'scorpio'\n",
    "elif month == 'november':\n",
    "\tastro_sign = 'scorpio' if (day < 22) else 'sagittarius'\n",
    "print(\"Your Astrological sign is :\",astro_sign)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cced1cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2f079f7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter x*x coefficient:33\n",
      "enter x coefficient:66\n",
      "enter the constant term:-55\n",
      "the roots of equation: 2.632993161855452 -0.6329931618554521\n"
     ]
    }
   ],
   "source": [
    "#51:Roots of Quadratic Equation\n",
    "a=int(input(\"enter x*x coefficient:\"))\n",
    "b=int(input(\"enter x coefficient:\"))\n",
    "c=int(input(\"enter the constant term:\"))\n",
    "d=(b*b)-(4*a*c) #this is descriminant\n",
    "if d>0:\n",
    "    root_1=(b+(d**0.5))/(2*a)\n",
    "    root_2=(b-(d**0.5))/(2*a)\n",
    "    print(\"the roots of equation:\",root_1,root_2)\n",
    "else:\n",
    "    print(\"the roots of complex\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9dc96e8",
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
