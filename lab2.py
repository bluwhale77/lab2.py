{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7665b6a-bbb5-4b98-b190-58947641f7c1",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to PyCalc!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter left operand:  four\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This code only works with integers.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter left operand:  four\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This code only works with integers.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter left operand:  4\n",
      "Enter right operand:  two\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This code only works with integers.\n"
     ]
    }
   ],
   "source": [
    "#lab2.py\n",
    "\n",
    "# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python\n",
    "# Please see the README in this repository for the requirements of this lab exercise\n",
    "\n",
    "# Bryant Lu\n",
    "# Lubg@uci.edu\n",
    "# 83665984\n",
    "\n",
    "def add(a, b):\n",
    "    return  a + b\n",
    "\n",
    "def sub(a, b):\n",
    "    return  a - b\n",
    "\n",
    "def div(a, b):\n",
    "    return  a / b\n",
    "\n",
    "def mul(a, b):\n",
    "    return  a * b\n",
    "\n",
    "def run():\n",
    "    try:\n",
    "        a = int(input(\"Enter left operand: \"))\n",
    "    except ValueError:\n",
    "        print(\"This code only works with integers.\")\n",
    "        run()\n",
    "    try:\n",
    "        b = int(input(\"Enter right operand: \"))\n",
    "    except ValueError:\n",
    "        print(\"This code only works with integers.\")\n",
    "        run()\n",
    "    operator = input(\"What type of calculation would you like to perform (+, -, x, /)? \")\n",
    "    \n",
    "    r = 0\n",
    "\n",
    "    try:\n",
    "        if operator == \"+\":\n",
    "            r = add(int(a),int(b))\n",
    "        elif operator == \"-\":\n",
    "            r = sub(int(a),int(b))\n",
    "        elif operator == \"x\":\n",
    "            r = mul(int(a),int(b))\n",
    "        elif operator == \"/\":\n",
    "            r = div(int(a),int(b))\n",
    "        else:\n",
    "            r = \"Unable to perform the desired calculation, please try again.\"\n",
    "        print(r)\n",
    "    except ZeroDivisionError:\n",
    "        print(\"Divison by zero is undefined.\")\n",
    "    \n",
    "    \n",
    "    \n",
    "    if input(\"Run another calculation (y/n)? \") == \"y\":\n",
    "        run()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"Welcome to PyCalc!\")\n",
    "    run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb40fb03-ac70-4b2e-8bfc-49be8e78e180",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
