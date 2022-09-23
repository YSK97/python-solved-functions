{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f9ab786",
   "metadata": {},
   "outputs": [],
   "source": [
    "#list problems\n",
    "#1:sort list\n",
    "n=int(input('enter first number'))\n",
    "mylist=list()\n",
    "while n!=0:\n",
    "    mylist.append(n)\n",
    "n=int(input('enter next number'))\n",
    "print(mylist)\n",
    "mylist.sort()\n",
    "print(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b1615c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first number10\n"
     ]
    }
   ],
   "source": [
    "#2:reverse order\n",
    "n=int(input('enter first number'))\n",
    "mylist=list()\n",
    "while n!=0:\n",
    "    mylist.append(n)\n",
    "n=int(input('enter next number'))\n",
    "print(mylist)\n",
    "mylist.reverse()\n",
    "print(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "38931cc5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "#4;Negative Zero Positive \n",
    "# Python program to print negative Numbers in a List\n",
    "\n",
    "# list of numbers\n",
    "list1 = [11, -21, 0, 45, 66, -93]\n",
    "res=[]\n",
    "list2=list(map(str,list1))\n",
    "for i in range(0,len(list2)):\n",
    "\tif(list2[i].startswith(\"-0+\")):\n",
    "\t\tres.append(str(list1[i]))\n",
    "res=\" \".join(res)\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e2e95cf",
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
