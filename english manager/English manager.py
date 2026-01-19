import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
import random
import time

# ------------------- Расширенные данные уроков -------------------
lessons_data = {
    "новичок": {
        "базовый": [
            {"word": "cat", "options": ["кот", "собака", "дом"], "answer": "кот", "hint": "Животное, которое мурлычет"},
            {"word": "dog", "options": ["собака", "кошка", "солнце"], "answer": "собака", "hint": "Лучший друг человека"},
            {"word": "sun", "options": ["луна", "солнце", "звезда"], "answer": "солнце", "hint": "Дает свет днем"},
            {"word": "book", "options": ["книга", "ручка", "стол"], "answer": "книга", "hint": "Что читают для знаний?"},
            {"word": "house", "options": ["дом", "крыша", "окно"], "answer": "дом", "hint": "Место, где живут люди"}
        ],
        "средний": [
            {"word": "apple", "options": ["яблоко", "апельсин", "банан"], "answer": "яблоко", "hint": "Фрукт, который упал на Ньютона"},
            {"word": "water", "options": ["вода", "молоко", "сок"], "answer": "вода", "hint": "H₂O, источник жизни"},
            {"word": "friend", "options": ["друг", "враг", "знакомый"], "answer": "друг", "hint": "Тот, кто всегда поддержит"},
            {"word": "school", "options": ["школа", "университет", "детский сад"], "answer": "школа", "hint": "Место, где учатся дети"},
            {"word": "family", "options": ["семья", "друзья", "коллеги"], "answer": "семья", "hint": "Родные люди"}
        ],
        "сложный": [
            {"word": "morning", "options": ["утро", "вечер", "ночь"], "answer": "утро", "hint": "Начало дня"},
            {"word": "evening", "options": ["вечер", "день", "полдень"], "answer": "вечер", "hint": "Время после дня"},
            {"word": "garden", "options": ["сад", "парк", "лес"], "answer": "сад", "hint": "Место с цветами около дома"},
            {"word": "window", "options": ["окно", "дверь", "стена"], "answer": "окно", "hint": "Через него смотрят на улицу"},
            {"word": "kitchen", "options": ["кухня", "спальня", "гостиная"], "answer": "кухня", "hint": "Готовят еду"}
        ]
    },
    "средний": {
        "базовый": [
            {"word": "elephant", "options": ["слон", "зебра", "коала"], "answer": "слон", "hint": "Самое большое сухопутное животное"},
            {"word": "computer", "options": ["компьютер", "телефон", "планшет"], "answer": "компьютер", "hint": "Устройство для программирования"},
            {"word": "university", "options": ["университет", "школа", "магазин"], "answer": "университет", "hint": "Высшее учебное заведение"},
            {"word": "mountain", "options": ["гора", "река", "лес"], "answer": "гора", "hint": "Эверест - самая высокая..."},
            {"word": "language", "options": ["язык", "книга", "письмо"], "answer": "язык", "hint": "Средство общения между людьми"}
        ],
        "средний": [
            {"word": "freedom", "options": ["свобода", "мир", "любовь"], "answer": "свобода", "hint": "Право делать свой выбор"},
            {"word": "weather", "options": ["погода", "климат", "температура"], "answer": "погода", "hint": "Состояние атмосферы"},
            {"word": "holiday", "options": ["отпуск", "работа", "учеба"], "answer": "отпуск", "hint": "Время отдыха от работы"},
            {"word": "journey", "options": ["путешествие", "дорога", "прогулка"], "answer": "путешествие", "hint": "Поездка в другое место"},
            {"word": "knowledge", "options": ["знание", "умение", "опыт"], "answer": "знание", "hint": "То, что знает человек"}
        ],
        "сложный": [
            {"word": "opportunity", "options": ["возможность", "проблема", "задача"], "answer": "возможность", "hint": "Шанс что-то сделать"},
            {"word": "challenge", "options": ["вызов", "проблема", "задание"], "answer": "вызов", "hint": "Сложная задача"},
            {"word": "environment", "options": ["окружающая среда", "природа", "экология"], "answer": "окружающая среда", "hint": "Все что нас окружает"},
            {"word": "development", "options": ["развитие", "рост", "прогресс"], "answer": "развитие", "hint": "Процесс улучшения"},
            {"word": "communication", "options": ["общение", "разговор", "диалог"], "answer": "общение", "hint": "Обмен информацией"}
        ]
    },
    "продвинутый": {
        "базовый": [
            {"word": "philosophy", "options": ["философия", "психология", "история"], "answer": "философия", "hint": "Наука о фундаментальных вопросах бытия"},
            {"word": "psychology", "options": ["психология", "метафора", "литература"], "answer": "психология", "hint": "Наука о душе и поведении"},
            {"word": "metaphor", "options": ["метафора", "концепция", "идея"], "answer": "метафора", "hint": "Сравнение без слов 'как' или 'словно'"},
            {"word": "consequence", "options": ["последствие", "причина", "шанс"], "answer": "последствие", "hint": "Результат какого-либо действия"},
            {"word": "achievement", "options": ["достижение", "провал", "успех"], "answer": "достижение", "hint": "То, чего удалось добиться"}
        ],
        "средний": [
            {"word": "complexity", "options": ["сложность", "простота", "проблема"], "answer": "сложность", "hint": "Качество сложного, многосоставного"},
            {"word": "interpretation", "options": ["толкование", "анализ", "решение"], "answer": "толкование", "hint": "Объяснение смысла чего-либо"},
            {"word": "perspective", "options": ["перспектива", "фокус", "объектив"], "answer": "перспектива", "hint": "Вид вдаль, точка зрения"},
            {"word": "controversy", "options": ["спор", "дискуссия", "согласие"], "answer": "спор", "hint": "Обсуждение с разными мнениями"},
            {"word": "ambiguity", "options": ["неоднозначность", "ясность", "простота"], "answer": "неоднозначность", "hint": "Имеющий несколько значений"}
        ],
        "сложный": [
            {"word": "sophisticated", "options": ["изощренный", "простой", "обычный"], "answer": "изощренный", "hint": "Сложный, утонченный"},
            {"word": "comprehensive", "options": ["всесторонний", "ограниченный", "частичный"], "answer": "всесторонний", "hint": "Полный, охватывающий все"},
            {"word": "multifaceted", "options": ["многогранный", "односторонний", "плоский"], "answer": "многогранный", "hint": "Имеющий много аспектов"},
            {"word": "unprecedented", "options": ["беспрецедентный", "обычный", "типичный"], "answer": "беспрецедентный", "hint": "Не имеющий прецедентов"},
            {"word": "paradigm", "options": ["парадигма", "модель", "пример"], "answer": "парадигма", "hint": "Совокупность фундаментальных установок"}
        ]
    }
}

rules_data = {
    "новичок": "📘 Present Simple используется для:\n\n• Повседневных действий (I work every day)\n• Общеизвестных фактов (The sun rises in the east)\n• Постоянных состояний (She lives in London)\n• Расписаний и программ (The train leaves at 8 PM)",
    "средний": "📗 Past Simple используется для:\n\n• Завершённых действий в прошлом (I visited Paris last year)\n• Последовательных событий в рассказе\n• Привычек в прошлом (When I was a child, I played football)\n• Конкретных моментов времени (She called me yesterday)",
    "продвинутый": "🚀 Условные предложения (Conditionals):\n\n• Zero Conditional: If you heat ice, it melts (факты)\n• First Conditional: If it rains, I will stay home (реальные будущие ситуации)\n• Second Conditional: If I were rich, I would travel the world (нереальные настоящие/будущие)\n• Third Conditional: If I had studied, I would have passed (нереальные прошлые)"
}

# ------------------- Пользователь -------------------
class User:
    def __init__(self, name, level=""):
        self.name = name
        self.level = level
        self.history = []
        self.stats = {
            "correct": 0,
            "incorrect": 0,
            "lessons_completed": 0,
            "total_time_spent": 0,
            "average_time_per_question": 0,
            "last_active": "",
            "current_difficulty": "базовый",
            "progress": 0  # от 0 до 100
        }
        self.achievements = []

    def save(self):
        data = {
            "name": self.name,
            "level": self.level,
            "history": self.history,
            "stats": self.stats,
            "achievements": self.achievements
        }
        os.makedirs("users", exist_ok=True)
        with open(f"users/{self.name}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load(name):
        filename = f"users/{name}.json"
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            user = User(data["name"], data["level"])
            user.history = data.get("history", [])
            user.stats = data.get("stats", {
                "correct": 0, "incorrect": 0, 
                "lessons_completed": 0, "total_time_spent": 0,
                "average_time_per_question": 0, "last_active": "",
                "current_difficulty": "базовый",
                "progress": 0
            })
            user.achievements = data.get("achievements", [])
            return user
        except:
            return None
    
    def update_difficulty(self, score):
        """Обновляет сложность в зависимости от результатов"""
        if score >= 80:
            # Отличный результат - повышаем сложность
            if self.stats["current_difficulty"] == "базовый":
                self.stats["current_difficulty"] = "средний"
                self.stats["progress"] = 33
            elif self.stats["current_difficulty"] == "средний":
                self.stats["current_difficulty"] = "сложный"
                self.stats["progress"] = 66
            elif self.stats["current_difficulty"] == "сложный":
                self.stats["progress"] = 100
        elif score < 50:
            # Плохой результат - понижаем сложность
            if self.stats["current_difficulty"] == "сложный":
                self.stats["current_difficulty"] = "средний"
                self.stats["progress"] = 33
            elif self.stats["current_difficulty"] == "средний":
                self.stats["current_difficulty"] = "базовый"
                self.stats["progress"] = 0
        
        self.save()

# ------------------- Анимационные эффекты -------------------
class Animations:
    @staticmethod
    def typewriter_effect(label, text, delay=50, callback=None):
        """Эффект печатной машинки"""
        label.config(text="")
        
        def type_char(i=0):
            if i < len(text):
                label.config(text=text[:i+1])
                label.after(delay, lambda: type_char(i + 1))
            elif callback:
                label.after(100, callback)
        
        type_char()

# ------------------- Приложение -------------------
class EnglishApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ English Learning Pro")
        self.root.geometry("1000x750")
        
        # Стили для приложения
        self.colors = {
            "primary": "#667eea",
            "secondary": "#764ba2",
            "accent": "#f093fb",
            "success": "#4ade80",
            "error": "#f87171",
            "warning": "#fbbf24",
            "dark": "#1e293b",
            "light": "#f8fafc",
            "card": "#ffffff"
        }
        
        self.root.configure(bg=self.colors["light"])
        
        # Используем стандартные шрифты
        self.title_font = ("Arial", 24, "bold")
        self.normal_font = ("Arial", 12)
        self.large_font = ("Arial", 16)
        self.xlarge_font = ("Arial", 36, "bold")
        
        self.user = None
        self.lesson_index = 0
        self.current_lesson_list = []
        self.question_start_time = None
        self.lesson_start_time = None
        self.question_times = []
        self.correct_answers = 0
        self.total_questions = 0
        
        # Главный контейнер
        self.main_container = tk.Frame(root, bg=self.colors["light"])
        self.main_container.pack(fill="both", expand=True)
        
        self.show_intro()

    def clear_frame(self):
        """Очищает основной контейнер"""
        for widget in self.main_container.winfo_children():
            widget.destroy()

    # ---------- Ввод имени ----------
    def show_intro(self):
        self.clear_frame()
        
        # Создаем фон
        canvas = tk.Canvas(self.main_container, width=1000, height=750, 
                          bg=self.colors["primary"], highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Контент поверх фона
        content_frame = tk.Frame(canvas, bg="white", bd=0)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", 
                          width=500, height=500)
        
        # Анимированный заголовок
        title_label = tk.Label(content_frame, text="", 
                              font=self.title_font,
                              bg="white", fg=self.colors["dark"])
        title_label.pack(pady=(40, 10))
        Animations.typewriter_effect(title_label, "🌟 English Master", 80)
        
        # ЯВНАЯ ПОДСКАЗКА - КРУПНЫЙ ТЕКСТ
        tk.Label(content_frame, 
                text="Для начала работы введите ваше имя в поле ниже:",
                font=("Arial", 14, "bold"), 
                bg="white", fg=self.colors["primary"]).pack(pady=20)
        
        # Рамка с иконкой и полем ввода
        input_frame = tk.Frame(content_frame, bg="white", bd=2, 
                              relief="groove", padx=10, pady=10)
        input_frame.pack(pady=20)
        
        # Иконка
        icon_label = tk.Label(input_frame, text="👤", font=("Arial", 24), 
                             bg="white")
        icon_label.pack(side="left", padx=10)
        
        # Подсказка над полем ввода
        tk.Label(input_frame, text="Ваше имя:", 
                font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
        
        # Поле ввода
        self.name_entry = tk.Entry(input_frame, font=self.large_font,
                                  width=25, bd=2, relief="flat",
                                  highlightbackground=self.colors["primary"],
                                  highlightthickness=2)
        self.name_entry.pack(pady=5)
        self.name_entry.focus()
        self.name_entry.bind("<Return>", lambda e: self.get_name())
        
        # Дополнительная подсказка под полем
        tk.Label(content_frame, text="Имя будет использоваться для сохранения вашего прогресса",
                font=("Arial", 10), bg="white", fg="#64748b").pack(pady=10)
        
        # Анимированная кнопка
        btn = tk.Button(content_frame, text="🚀 Начать обучение", 
                       font=self.large_font,
                       bg=self.colors["primary"], fg="white",
                       padx=30, pady=12, bd=0, cursor="hand2",
                       command=self.get_name)
        btn.pack(pady=20)
        
        # Эффект при наведении
        def on_enter(e):
            btn.config(bg=self.colors["secondary"])
        def on_leave(e):
            btn.config(bg=self.colors["primary"])
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def get_name(self):
        name = self.name_entry.get().strip()
        
        # Проверяем, не пустое ли имя
        if not name:
            # Анимация для привлечения внимания к полю ввода
            self.name_entry.config(bg="#ffebee")
            self.root.after(100, lambda: self.name_entry.config(bg="white"))
            self.root.after(200, lambda: self.name_entry.config(bg="#ffebee"))
            self.root.after(300, lambda: self.name_entry.config(bg="white"))
            
            messagebox.showwarning("Внимание", "Пожалуйста, введите ваше имя!")
            self.name_entry.focus()
            return
            
        self.user = User.load(name)
        if self.user is None:
            self.user = User(name, "")
            self.show_level_choice()
        else:
            self.show_welcome_back()

    # ---------- Приветствие вернувшегося ----------
    def show_welcome_back(self):
        self.clear_frame()
        
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#4ade80", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        content_frame = tk.Frame(canvas, bg="white", bd=0)
        content_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=600, height=450)
        
        # Приветствие с анимацией
        welcome_label = tk.Label(content_frame, text="", 
                                font=self.title_font,
                                bg="white", fg=self.colors["dark"])
        welcome_label.pack(pady=(40, 10))
        Animations.typewriter_effect(welcome_label, f"Рады снова видеть, {self.user.name}!", 60)
        
        # Статистика в карточках
        stats = self.user.stats
        total = stats["correct"] + stats["incorrect"]
        accuracy = (stats["correct"] / total * 100) if total > 0 else 0
        
        stats_frame = tk.Frame(content_frame, bg="white")
        stats_frame.pack(pady=30)
        
        stats_data = [
            ("📊", "Правильных ответов", f"{stats['correct']}"),
            ("🎯", "Точность", f"{accuracy:.1f}%"),
            ("⏱️", "Ср. время ответа", f"{stats.get('average_time_per_question', 0):.1f}с"),
            ("⭐", "Уроков пройдено", f"{stats['lessons_completed']}")
        ]
        
        for icon, label, value in stats_data:
            card = tk.Frame(stats_frame, bg="#f8fafc", bd=1, 
                           relief="ridge", padx=15, pady=10)
            card.pack(side="left", padx=10, fill="y")
            
            tk.Label(card, text=icon, font=("Arial", 20), 
                    bg="#f8fafc").pack()
            tk.Label(card, text=label, font=("Arial", 10),
                    bg="#f8fafc", fg="#64748b").pack()
            tk.Label(card, text=value, font=("Arial", 16, "bold"),
                    bg="#f8fafc", fg=self.colors["primary"]).pack()
        
        # Кнопки действий с кнопкой НАЗАД
        btn_frame = tk.Frame(content_frame, bg="white")
        btn_frame.pack(pady=40)
        
        # Кнопка Назад (влево)
        back_btn = tk.Button(btn_frame, text="← Назад", 
                            font=self.normal_font, bg="#94a3b8",
                            fg="white", padx=25, pady=10,
                            command=self.show_intro)
        back_btn.pack(side="left", padx=10)
        
        continue_btn = tk.Button(btn_frame, text="▶️ Продолжить", 
                               font=self.normal_font, bg=self.colors["success"],
                               fg="white", padx=25, pady=10,
                               command=self.animate_hello)
        continue_btn.pack(side="left", padx=10)
        
        change_btn = tk.Button(btn_frame, text="⚙️ Изменить уровень", 
                              font=self.normal_font, bg=self.colors["warning"],
                              fg="white", padx=25, pady=10,
                              command=self.show_level_choice)
        change_btn.pack(side="left", padx=10)

    # ---------- Выбор уровня ----------
    def show_level_choice(self):
        self.clear_frame()
        
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#8b5cf6", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        content_frame = tk.Frame(canvas, bg="white", bd=0)
        content_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=700, height=550)
        
        # Кнопка Назад в верхнем левом углу
        back_btn = tk.Button(content_frame, text="← Назад", 
                            font=("Arial", 10), bg="#94a3b8", fg="white",
                            padx=15, pady=5, command=self.show_intro)
        back_btn.place(x=10, y=10)
        
        tk.Label(content_frame, text="🎯 Выбери уровень сложности", 
                font=self.title_font, bg="white").pack(pady=30)
        
        # Уровни
        levels = [
            ("🔰", "Новичок", "#4ade80", "Основы языка, простые слова и фразы"),
            ("🎯", "Средний", "#3b82f6", "Разговорная практика, времена глаголов"),
            ("🚀", "Продвинутый", "#8b5cf6", "Сложные конструкции, идиомы")
        ]
        
        for icon, name, color, desc in levels:
            level_card = tk.Frame(content_frame, bg="#f8fafc", 
                                 bd=1, relief="ridge")
            level_card.pack(fill="x", padx=50, pady=8, ipadx=20, ipady=15)
            
            # Заголовок карточки
            header = tk.Frame(level_card, bg=color)
            header.pack(fill="x", pady=(0, 10))
            tk.Label(header, text=f"{icon} {name}", 
                    font=("Arial", 16, "bold"), 
                    bg=color, fg="white", padx=15, pady=8).pack()
            
            # Описание
            tk.Label(level_card, text=desc, font=("Arial", 12),
                    bg="#f8fafc", wraplength=500).pack(pady=5)
            
            # Кнопка выбора
            btn = tk.Button(level_card, text="Выбрать →",
                           font=("Arial", 11), bg=color, fg="white",
                           command=lambda n=name.lower(): self.set_level(n))
            btn.pack(pady=10)

    def set_level(self, level):
        self.user.level = level
        self.user.save()
        self.animate_hello()

    # ---------- Анимация приветствия ----------
    def animate_hello(self):
        self.clear_frame()
        
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#f59e0b", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        greeting_label = tk.Label(canvas, text="", 
                                 font=("Arial", 36, "bold"),
                                 bg="white", fg=self.colors["dark"])
        greeting_label.place(relx=0.5, rely=0.4, anchor="center")
        
        # Анимация с несколькими фразами
        phrases = [
            "✨ Приготовься!",
            f"👋 {self.user.name}, ты готов?",
            "🎯 Начинаем урок!",
            "3...",
            "2...",
            "1...",
            "GO! 🚀"
        ]
        
        def animate_phrase(index):
            if index < len(phrases):
                greeting_label.config(text="", bg="white")
                # Эффект печатной машинки
                Animations.typewriter_effect(greeting_label, phrases[index], 70)
                self.root.after(len(phrases[index]) * 70 + 800, 
                              lambda: animate_phrase(index + 1))
            else:
                self.root.after(500, self.start_lesson)
        
        animate_phrase(0)

    # ---------- Старт урока ----------
    def start_lesson(self):
        self.lesson_index = 0
        self.correct_answers = 0
        self.total_questions = 0
        self.question_times = []
        self.lesson_start_time = datetime.now()
        
        # Берем вопросы соответствующей сложности
        difficulty = self.user.stats["current_difficulty"]
        self.current_lesson_list = lessons_data[self.user.level][difficulty].copy()
        random.shuffle(self.current_lesson_list)
        self.show_next_word()

    # ---------- Показ слова ----------
    def show_next_word(self):
        self.clear_frame()
        
        if self.lesson_index >= len(self.current_lesson_list):
            self.finish_lesson()
            return
            
        current = self.current_lesson_list[self.lesson_index]
        self.total_questions += 1
        self.question_start_time = datetime.now()
        
        # Фон
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#a78bfa", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Основной контент
        main_frame = tk.Frame(canvas, bg="white", bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center",
                        width=800, height=600)
        
        # Верхняя панель с кнопкой профиля и НАЗАД
        top_frame = tk.Frame(main_frame, bg="white")
        top_frame.pack(fill="x", pady=10, padx=30)
        
        # Кнопка Назад слева
        back_btn = tk.Button(top_frame, text="← Назад", 
                            font=("Arial", 10), bg="#e2e8f0",
                            command=self.show_profile)
        back_btn.pack(side="left", padx=(0, 10))
        
        # Кнопка профиля
        profile_btn = tk.Button(top_frame, text="👤 Профиль", 
                               font=("Arial", 10), bg="#e2e8f0",
                               command=self.show_profile)
        profile_btn.pack(side="left")
        
        # Прогресс справа
        progress_frame = tk.Frame(top_frame, bg="white")
        progress_frame.pack(side="right")
        
        progress = (self.lesson_index / len(self.current_lesson_list)) * 100
        tk.Label(progress_frame, 
                text=f"Вопрос {self.lesson_index + 1}/{len(self.current_lesson_list)}",
                font=("Arial", 12), bg="white").pack()
        
        # Прогресс-бар
        progress_canvas = tk.Canvas(progress_frame, width=200, height=8,
                                   bg="#e2e8f0", highlightthickness=0)
        progress_canvas.pack(pady=5)
        progress_canvas.create_rectangle(0, 0, 2 * progress, 8,
                                       fill="#4ade80", outline="")
        
        # Время и подсказка
        info_frame = tk.Frame(main_frame, bg="white")
        info_frame.pack(pady=10)
        
        # Таймер для вопроса
        self.time_label = tk.Label(info_frame, text="⏱️ 0.0с",
                                  font=("Arial", 12), bg="white", fg="#64748b")
        self.time_label.pack()
        
        # Обновление таймера в реальном времени
        def update_timer():
            if self.question_start_time:
                elapsed = (datetime.now() - self.question_start_time).total_seconds()
                self.time_label.config(text=f"⏱️ {elapsed:.1f}с")
                self.root.after(100, update_timer)
        
        update_timer()
        
        # Подсказка
        if "hint" in current:
            hint_label = tk.Label(info_frame, text=f"💡 {current['hint']}",
                                 font=("Arial", 10), bg="white", fg="#94a3b8",
                                 wraplength=300)
            hint_label.pack(pady=5)
        
        # Английское слово с анимацией
        word_frame = tk.Frame(main_frame, bg="white")
        word_frame.pack(pady=40)
        
        self.word_label = tk.Label(word_frame, text="", 
                                  font=self.xlarge_font,
                                  bg="white", fg=self.colors["dark"])
        self.word_label.pack()
        
        # Анимация появления слова
        def animate_word():
            full_word = current["word"].upper()
            Animations.typewriter_effect(self.word_label, full_word, 100)
        
        self.root.after(300, animate_word)
        
        # Варианты ответа
        options_frame = tk.Frame(main_frame, bg="white")
        options_frame.pack(pady=30)
        
        options = current["options"].copy()
        random.shuffle(options)
        
        colors = ["#4ade80", "#3b82f6", "#8b5cf6", "#f59e0b"]
        
        for idx, opt in enumerate(options):
            btn = tk.Button(options_frame, text=opt,
                          font=("Arial", 14), width=25,
                          bg=colors[idx % len(colors)], fg="white",
                          padx=20, pady=15, bd=0, cursor="hand2",
                          command=lambda o=opt: self.check_answer(o))
            btn.pack(pady=10)
            
            # Анимация появления кнопок с задержкой
            self.root.after(idx * 100, lambda b=btn: b.pack(pady=10))

    def check_answer(self, answer):
        # Фиксируем время ответа
        answer_time = (datetime.now() - self.question_start_time).total_seconds()
        self.question_times.append(answer_time)
        
        current = self.current_lesson_list[self.lesson_index]
        correct = current["answer"]
        
        # Анимация проверки
        if answer == correct:
            self.correct_answers += 1
            messagebox.showinfo("✅ Великолепно!", 
                              f"Правильно! '{current['word']}' = '{correct}'\n"
                              f"Время: {answer_time:.1f} секунд")
        else:
            messagebox.showerror("❌ Почти!", 
                               f"Правильный ответ: '{correct}'\n"
                               f"Вы выбрали: '{answer}'\n"
                               f"Время: {answer_time:.1f} секунд")
        
        self.lesson_index += 1
        self.show_next_word()

    # ---------- Завершение урока ----------
    def finish_lesson(self):
        self.clear_frame()
        
        # Подсчет статистики
        total_time = (datetime.now() - self.lesson_start_time).total_seconds()
        score = (self.correct_answers / self.total_questions) * 100 if self.total_questions > 0 else 0
        avg_time = sum(self.question_times) / len(self.question_times) if self.question_times else 0
        
        # Обновляем сложность в зависимости от результатов
        old_difficulty = self.user.stats["current_difficulty"]
        self.user.update_difficulty(score)
        new_difficulty = self.user.stats["current_difficulty"]
        
        # Обновление статистики пользователя
        self.user.stats["correct"] += self.correct_answers
        self.user.stats["incorrect"] += (self.total_questions - self.correct_answers)
        self.user.stats["lessons_completed"] += 1
        self.user.stats["total_time_spent"] += total_time
        
        # Обновляем среднее время
        total_answers = self.user.stats["correct"] + self.user.stats["incorrect"]
        if total_answers > 0:
            self.user.stats["average_time_per_question"] = (
                self.user.stats["total_time_spent"] / total_answers
            )
        
        self.user.stats["last_active"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Сохранение истории
        lesson_words = [item["word"] for item in self.current_lesson_list]
        self.user.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "level": self.user.level,
            "difficulty": old_difficulty,
            "words": lesson_words,
            "score": score,
            "time_spent": total_time,
            "avg_time_per_question": avg_time,
            "question_times": self.question_times.copy()
        })
        
        # Проверка достижений
        self.check_achievements()
        self.user.save()
        
        # Отображение результатов
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#8b5cf6", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        result_frame = tk.Frame(canvas, bg="white", bd=0)
        result_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=700, height=600)
        
        # Кнопка Назад в верхнем левом углу
        back_btn = tk.Button(result_frame, text="← Назад", 
                            font=("Arial", 10), bg="#94a3b8", fg="white",
                            padx=15, pady=5, command=self.show_profile)
        back_btn.place(x=10, y=10)
        
        # Анимированный результат
        if score >= 80:
            result_icon = "🏆"
            result_color = "#f59e0b"
            result_text = "Отлично!"
        elif score >= 60:
            result_icon = "🎯"
            result_color = "#3b82f6"
            result_text = "Хорошо!"
        else:
            result_icon = "💪"
            result_color = "#ef4444"
            result_text = "Продолжай тренироваться!"
        
        tk.Label(result_frame, text=result_icon, font=("Arial", 72),
                bg="white").pack(pady=20)
        
        result_label = tk.Label(result_frame, text="",
                               font=("Arial", 28, "bold"),
                               bg="white", fg=result_color)
        result_label.pack(pady=10)
        Animations.typewriter_effect(result_label, result_text, 80)
        
        # Детальная статистика
        stats_text = f"""
        📊 Результаты урока:
        
        Правильных ответов: {self.correct_answers}/{self.total_questions}
        Оценка: {score:.1f}%
        Общее время: {total_time:.1f} секунд
        Среднее время на вопрос: {avg_time:.1f} секунд
        
        Уровень: {self.user.level}
        Сложность: {old_difficulty} → {new_difficulty}
        Прогресс: {self.user.stats['progress']}%
        """
        
        tk.Label(result_frame, text=stats_text, font=("Arial", 14),
                bg="white", justify="left").pack(pady=20)
        
        # Сообщение о изменении сложности
        if old_difficulty != new_difficulty:
            diff_message = f"🎉 Сложность изменена: {old_difficulty} → {new_difficulty}!"
            if new_difficulty == "сложный":
                diff_message += "\nВы достигли максимальной сложности!"
            
            tk.Label(result_frame, text=diff_message, 
                    font=("Arial", 12, "bold"), bg="white", 
                    fg=self.colors["success"]).pack(pady=10)
        
        # Кнопки действий - только 2 кнопки как вы просили
        btn_frame = tk.Frame(result_frame, bg="white")
        btn_frame.pack(pady=30)
        
        # Первая кнопка - Выйти в профиль
        profile_btn = tk.Button(btn_frame, text="📊 Перейти в профиль", 
                               font=("Arial", 14, "bold"),
                               bg=self.colors["success"], fg="white",
                               padx=30, pady=12,
                               command=self.show_profile)
        profile_btn.pack(side="left", padx=20, pady=10)
        
        # Вторая кнопка - Начать заново
        restart_btn = tk.Button(btn_frame, text="🔄 Начать заново", 
                               font=("Arial", 14, "bold"),
                               bg=self.colors["primary"], fg="white",
                               padx=30, pady=12,
                               command=self.start_lesson)
        restart_btn.pack(side="left", padx=20, pady=10)

    # ---------- Проверка достижений ----------
    def check_achievements(self):
        stats = self.user.stats
        achievements = self.user.achievements
        
        new_achievements = []
        
        conditions = [
            (stats["lessons_completed"] >= 1, "Первый урок", "🎉"),
            (stats["correct"] >= 10, "10 правильных ответов", "✅"),
            (stats["lessons_completed"] >= 3, "Три урока", "📚"),
            (stats["total_time_spent"] >= 300, "5 минут обучения", "⏱️"),
            (self.correct_answers == len(self.current_lesson_list), "Без ошибок!", "🌟"),
            (sum(self.question_times)/len(self.question_times) < 3 if self.question_times else False, 
             "Скорострел", "⚡"),
            (stats["current_difficulty"] == "сложный", "Мастер сложности", "🏆"),
            (stats["progress"] >= 100, "Завершил уровень", "🎓")
        ]
        
        for condition, achievement, icon in conditions:
            if condition and achievement not in achievements:
                new_achievements.append(f"{icon} {achievement}")
                achievements.append(achievement)
        
        if new_achievements:
            messagebox.showinfo("🎉 Новые достижения!", 
                              "\n".join(new_achievements))

    # ---------- Профиль ----------
    def show_profile(self):
        self.clear_frame()
        
        canvas = tk.Canvas(self.main_container, width=1000, height=750,
                          bg="#6366f1", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Основной контент
        profile_frame = tk.Frame(canvas, bg="white", bd=0)
        profile_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=900, height=650)
        
        # Кнопка Назад в верхнем левом углу
        back_btn = tk.Button(profile_frame, text="← Назад", 
                            font=("Arial", 10), bg="#94a3b8", fg="white",
                            padx=15, pady=5, command=self.show_intro)
        back_btn.place(x=10, y=10)
        
        # Заголовок профиля
        title_label = tk.Label(profile_frame, text=f"👤 Профиль: {self.user.name}",
                              font=("Arial", 26, "bold"), bg="white")
        title_label.pack(pady=30)
        
        # Две колонки
        columns_frame = tk.Frame(profile_frame, bg="white")
        columns_frame.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Левая колонка - статистика
        left_frame = tk.Frame(columns_frame, bg="#f8fafc", bd=1, relief="ridge")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        tk.Label(left_frame, text="📈 Статистика", 
                font=("Arial", 18, "bold"), bg="#f8fafc").pack(pady=20)
        
        stats = self.user.stats
        total_answers = stats["correct"] + stats["incorrect"]
        accuracy = (stats["correct"] / total_answers * 100) if total_answers > 0 else 0
        
        # Статистика
        stat_items = [
            ("🎯", "Уровень:", self.user.level),
            ("📊", "Пройдено уроков:", f"{stats['lessons_completed']}"),
            ("✅", "Правильных ответов:", f"{stats['correct']}"),
            ("❌", "Ошибок:", f"{stats['incorrect']}"),
            ("🎯", "Точность:", f"{accuracy:.1f}%"),
            ("⏱️", "Общее время:", f"{stats['total_time_spent'] // 60} мин"),
            ("⚡", "Ср. время ответа:", f"{stats.get('average_time_per_question', 0):.1f} сек"),
            ("🏆", "Текущая сложность:", stats["current_difficulty"]),
            ("📈", "Прогресс уровня:", f"{stats['progress']}%")
        ]
        
        for icon, label, value in stat_items:
            stat_row = tk.Frame(left_frame, bg="#f8fafc")
            stat_row.pack(fill="x", padx=20, pady=8)
            
            tk.Label(stat_row, text=icon, font=("Arial", 16), 
                    bg="#f8fafc", width=3).pack(side="left")
            tk.Label(stat_row, text=label, font=("Arial", 12),
                    bg="#f8fafc", width=20, anchor="w").pack(side="left")
            tk.Label(stat_row, text=value, font=("Arial", 12, "bold"),
                    bg="#f8fafc", fg=self.colors["primary"]).pack(side="left")
        
        # Правая колонка - история и достижения
        right_frame = tk.Frame(columns_frame, bg="#f8fafc", bd=1, relief="ridge")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Достижения
        tk.Label(right_frame, text="🏆 Достижения", 
                font=("Arial", 18, "bold"), bg="#f8fafc").pack(pady=(20, 10))
        
        achievements_frame = tk.Frame(right_frame, bg="#f8fafc")
        achievements_frame.pack(padx=20, pady=10, fill="x")
        
        if self.user.achievements:
            for achievement in self.user.achievements:
                tk.Label(achievements_frame, text=f"✨ {achievement}", 
                        font=("Arial", 11), bg="#f8fafc",
                        anchor="w").pack(fill="x", pady=3)
        else:
            tk.Label(achievements_frame, text="Достижения появятся здесь",
                    font=("Arial", 11), bg="#f8fafc", fg="#64748b").pack()
        
        # История уроков
        tk.Label(right_frame, text="📚 Последние уроки", 
                font=("Arial", 18, "bold"), bg="#f8fafc").pack(pady=(20, 10))
        
        # Прокручиваемая история
        history_canvas = tk.Canvas(right_frame, bg="#f8fafc", height=200,
                                  highlightthickness=0)
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", 
                                command=history_canvas.yview)
        history_frame = tk.Frame(history_canvas, bg="#f8fafc")
        
        history_canvas.configure(yscrollcommand=scrollbar.set)
        history_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        scrollbar.pack(side="right", fill="y")
        history_canvas.create_window((0, 0), window=history_frame, anchor="nw")
        
        # Добавляем уроки в историю
        for idx, lesson in enumerate(reversed(self.user.history[-5:])):
            lesson_card = tk.Frame(history_frame, bg="white", bd=1, relief="ridge")
            lesson_card.pack(fill="x", pady=5, padx=5)
            
            # Основная информация
            info_frame = tk.Frame(lesson_card, bg="white")
            info_frame.pack(fill="x", padx=10, pady=8)
            
            tk.Label(info_frame, text=f"{lesson['date']}", 
                    font=("Arial", 10), bg="white", fg="#64748b").pack(anchor="w")
            
            tk.Label(info_frame, 
                    text=f"Уровень: {lesson['level']} | Сложность: {lesson.get('difficulty', 'базовый')} | Оценка: {lesson['score']:.1f}%",
                    font=("Arial", 11), bg="white").pack(anchor="w")
            
            tk.Label(info_frame, text=f"Время: {lesson['time_spent']:.1f}с | Ср. время: {lesson.get('avg_time_per_question', 0):.1f}с",
                    font=("Arial", 10), bg="white", fg="#64748b").pack(anchor="w")
        
        history_frame.update_idletasks()
        history_canvas.config(scrollregion=history_canvas.bbox("all"))
        
        # Кнопки действий в профиле
        action_frame = tk.Frame(profile_frame, bg="white")
        action_frame.pack(side="bottom", pady=20)
        
        # Три основные кнопки
        tk.Button(action_frame, text="🎯 Продолжить обучение", 
                 font=("Arial", 14, "bold"), bg=self.colors["success"],
                 fg="white", padx=30, pady=12,
                 command=self.start_lesson).pack(side="left", padx=10)
        
        tk.Button(action_frame, text="⚙️ Изменить уровень", 
                 font=("Arial", 14), bg=self.colors["warning"],
                 fg="white", padx=30, pady=12,
                 command=self.show_level_choice).pack(side="left", padx=10)
        
        tk.Button(action_frame, text="↩️ На главную", 
                 font=("Arial", 14), bg="#94a3b8",
                 fg="white", padx=30, pady=12,
                 command=self.show_intro).pack(side="left", padx=10)

# ------------------- Запуск приложения -------------------
if __name__ == "__main__":
    root = tk.Tk()
    
    # Центрируем окно
    root.update_idletasks()
    width = 1000
    height = 750
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = EnglishApp(root)
    root.mainloop()