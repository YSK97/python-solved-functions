{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "72811921",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the row number22\n",
      "enter the column number22\n",
      "The square is BLACK colored\n"
     ]
    }
   ],
   "source": [
    "#46:Chess Board\n",
    "r=int(input('enter the row number'))\n",
    "c=int(input('enter the column number'))\n",
    "if (r%2==0 and c%2==0) or (r%2!=0 and c%2!=0):\n",
    "    print('The square is BLACK colored')\n",
    "else:\n",
    "    print('The square is WHITE colored')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "06002372",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3249761596.py, line 25)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [22]\u001b[1;36m\u001b[0m\n\u001b[1;33m    total price=base_charge+add_min_charge+add_msg_charge+call_center_price\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#57 Cell Phone Bill\n",
    "m=int(input('Enter the number of Minutes'))\n",
    "t=int(input('Enter number of text messages'))\n",
    "\n",
    "call_center_price=0.44\n",
    "tax=0.05\n",
    "if m<=50 and t<=50:\n",
    "    price=15\n",
    "    add_min_charge=0\n",
    "    add_msg_charge=0\n",
    "elif m>50 and t>50:\n",
    "    price1=(m-50)*0.25\n",
    "    price2=(t-50)*0.15\n",
    "    add_min_charge=price1\n",
    "    add_msg_charge=price2\n",
    "elif m>50:\n",
    "    price1=(m-50)*0.25\n",
    "    add_min_charge=price1\n",
    "    add_msg_charge=0\n",
    "elif t>50:\n",
    "    price2=(t-50)*0.15\n",
    "    add_min_charge=0\n",
    "    add_msg_charge=price1\n",
    "    \n",
    "total price=base_charge+add_min_charge+add_msg_charge+call_center_price\n",
    "total tax=total price*tax\n",
    "bill=total price+total tax\n",
    "print('the base charge:',base_charge)\n",
    "print('additional min charge:',add_min_charge)\n",
    "print('additional text msg charge:',add_msg_charge)\n",
    "print('call center charge:',call_center_price)\n",
    "print('tax amount:',total tax)\n",
    "print('total bill:',bill)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "87c0cc84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a year: 2000\n",
      "2000 is a leap year\n"
     ]
    }
   ],
   "source": [
    "#58: Python program to check if year is a leap year or not\n",
    "\n",
    "year = int(input(\"Enter a year: \"))\n",
    "if (year % 400 == 0) and (year % 100 == 0):\n",
    "    print(\"{0} is a leap year\".format(year))\n",
    "\n",
    "elif (year % 4 ==0) and (year % 100 != 0):\n",
    "    print(\"{0} is a leap year\".format(year))\n",
    "\n",
    "else:\n",
    "    print(\"{0} is not a leap year\".format(year))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f454402a",
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
