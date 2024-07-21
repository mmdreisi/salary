import tkinter as tk
from tkinter import messagebox

def calculate_budget():
    try:
       
        salary = float(entry_salary.get())
        debts = [float(entry_debt1.get()), float(entry_debt2.get()), float(entry_debt3.get()) , float(entry_debt4.get())]
        
        
        total_debts = sum(debts)
        
        
        remaining_salary = salary - total_debts
        
        
        rent_percentage = float(entry_rent_percentage.get()) / 100
        food_percentage = float(entry_food_percentage.get()) / 100
        savings_percentage = float(entry_savings_percentage.get()) / 100
        
        
        rent = remaining_salary * rent_percentage
        food = remaining_salary * food_percentage
        savings = remaining_salary * savings_percentage
        other_expenses = remaining_salary - (rent + food + savings)
        
        
        label_remaining_salary.config(text=f"باقیمانده حقوق: {remaining_salary:.2f} تومان")
        label_rent.config(text=f"هزینه اجاره: {rent:.2f} تومان")
        label_food.config(text=f"هزینه غذا: {food:.2f} تومان")
        label_savings.config(text=f"پس‌انداز: {savings:.2f} تومان")
        label_other.config(text=f"هزینه‌های دیگر: {other_expenses:.2f} تومان")
        
    except ValueError:
        messagebox.showerror("خطا", "لطفا مقادیر معتبر وارد کنید.")


root = tk.Tk()
root.title("مدیریت بودجه")
root.geometry("400x500") 

font_large = ("Arial", 14)


tk.Label(root, text="مبلغ حقوق:", font=font_large).grid(row=0, column=0, pady=5)
entry_salary = tk.Entry(root, font=font_large)
entry_salary.grid(row=0, column=1, pady=5)

tk.Label(root, text="قرض:", font=font_large).grid(row=1, column=0, pady=5)
entry_debt1 = tk.Entry(root, font=font_large)
entry_debt1.grid(row=1, column=1, pady=5)

tk.Label(root, text="ماشین:", font=font_large).grid(row=2, column=0, pady=5)
entry_debt2 = tk.Entry(root, font=font_large)
entry_debt2.grid(row=2, column=1, pady=5)


tk.Label(root, text="وام ها:", font=font_large).grid(row=3, column=0, pady=5)
entry_debt3 = tk.Entry(root, font=font_large)
entry_debt3.grid(row=3, column=1, pady=5)

tk.Label(root, text="هزینه اضطراری:", font=font_large).grid(row=2, column=0, pady=5)
entry_debt4 = tk.Entry(root, font=font_large)
entry_debt2.grid(row=2, column=1, pady=5)


tk.Label(root, text="درصد اجاره:", font=font_large).grid(row=4, column=0, pady=5)
entry_rent_percentage = tk.Entry(root, font=font_large)
entry_rent_percentage.grid(row=4, column=1, pady=5)


tk.Label(root, text="درصد غذا:", font=font_large).grid(row=5, column=0, pady=5)
entry_food_percentage = tk.Entry(root, font=font_large)
entry_food_percentage.grid(row=5, column=1, pady=5)

tk.Label(root, text="درصد پس‌انداز:", font=font_large).grid(row=6, column=0, pady=5)
entry_savings_percentage = tk.Entry(root, font=font_large)
entry_savings_percentage.grid(row=6, column=1, pady=5)


btn_calculate = tk.Button(root, text="محاسبه", command=calculate_budget, font=font_large)
btn_calculate.grid(row=7, column=0, columnspan=2, pady=10)

label_remaining_salary = tk.Label(root, text="باقیمانده حقوق: ", font=font_large)
label_remaining_salary.grid(row=8, column=0, columnspan=2, pady=5)

label_rent = tk.Label(root, text="هزینه اجاره: ", font=font_large)
label_rent.grid(row=9, column=0, columnspan=2, pady=5)

label_food = tk.Label(root, text="هزینه غذا: ", font=font_large)
label_food.grid(row=10, column=0, columnspan=2, pady=5)

label_savings = tk.Label(root, text="پس‌انداز: ", font=font_large)
label_savings.grid(row=11, column=0, columnspan=2, pady=5)

label_other = tk.Label(root, text="هزینه‌های دیگر: ", font=font_large)
label_other.grid(row=12, column=0, columnspan=2, pady=5)

root.mainloop()



