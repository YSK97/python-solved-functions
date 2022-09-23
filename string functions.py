{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c750b62f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any string:raju boy\n",
      "y o b   u j a r "
     ]
    }
   ],
   "source": [
    "#string function\n",
    "#write a program to reverse the given string.\n",
    "s=str(input(\"enter any string:\"))\n",
    "a=len(s)\n",
    "b=a-1\n",
    "for i in range(0,a):\n",
    "    print(s[b],end=' ')\n",
    "    b=b-1\n",
    "    if b<0:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "568e9f52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any string:raju\n",
      "u j a r "
     ]
    }
   ],
   "source": [
    "s=str(input(\"enter any string:\"))\n",
    "a=len(s)\n",
    "b=a-1\n",
    "while a>=0:\n",
    "    print(s[b],end=' ')\n",
    "    b=b-1\n",
    "    if b<0:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e3673fab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any string:raju boy\n",
      "yob ujar\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "s=str(input(\"enter any string:\"))\n",
    "print(s[::-1])\n",
    "print(s.count(' '))\n",
    "count=0\n",
    "for i in range(a):\n",
    "    if s[i]==' ':\n",
    "        count=count+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "31e4e4b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any string:my name is shiva krishna naidu\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "#no of words\n",
    "s=str(input(\"enter any string:\"))\n",
    "a=s.count(' ')\n",
    "words=a+1\n",
    "print(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "88460675",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 6.6, 7, 8, 9, ['a', 'b']] [7, 8, 9, ['a', 'b'], 1, 3, 6.6]\n",
      "[100, 3, 6.6]\n",
      "3 9 b\n"
     ]
    }
   ],
   "source": [
    "#list #mutable\n",
    "a=[1,3,6.6]\n",
    "b=[7,8,9,['a','b']]\n",
    "c=[]\n",
    "len(a)\n",
    "print(a+b,b+a)\n",
    "2*a\n",
    "a[0]=100\n",
    "print(a)\n",
    "print(a[1],b[2],b[3][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f627f709",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#tuple imutable\n",
    "t=(1,2,3)\n",
    "len(t)\n",
    "print(t[0])\n",
    "t[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "8fc2dac3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys([1, 2, 3])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "dict_values(['a', 'b', 'c'])"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#dictionary\n",
    "d={1:'a',2:'b',3:'c'}\n",
    "print(d.keys())\n",
    "d.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68701ad3",
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
