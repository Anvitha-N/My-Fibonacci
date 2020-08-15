{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many terms? 20\n",
      "Fibonacci sequence:\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n",
      "55\n",
      "89\n",
      "144\n",
      "233\n",
      "377\n",
      "610\n",
      "987\n",
      "1597\n",
      "2584\n",
      "4181\n"
     ]
    }
   ],
   "source": [
    "# Program to display the Fibonacci sequence up to n-th term\n",
    "\n",
    "nterms = int(input(\"How many terms? \"))\n",
    "\n",
    "# first two terms\n",
    "n1, n2 = 0, 1\n",
    "count = 0\n",
    "\n",
    "# check if the number of terms is valid\n",
    "if nterms <= 0:\n",
    "   print(\"Please enter a positive integer\")\n",
    "elif nterms == 1:\n",
    "   print(\"Fibonacci sequence upto\",nterms,\":\")\n",
    "   print(n1)\n",
    "else:\n",
    "   print(\"Fibonacci sequence:\")\n",
    "   while count < nterms:\n",
    "       print(n1)\n",
    "       nth = n1 + n2\n",
    "       # update values\n",
    "       n1 = n2\n",
    "       n2 = nth\n",
    "       count += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
