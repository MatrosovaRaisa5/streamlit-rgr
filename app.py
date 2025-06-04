import streamlit as st
from PIL import Image
import pandas as pd
from catboost import CatBoostClassifier

st.set_page_config(
    page_title="ML Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state='expanded'
)

if 'page' not in st.session_state:
    st.session_state.page = "О разработчике"

# Навигация
with st.sidebar:
    # Стили
    st.markdown("""
    <style>
    .sidebar-title {
        font-size: 28px !important;
        color: #2c3e50 !important;
        margin-bottom: 20px;
        text-align: center;
        padding-bottom: 10px;
        border-bottom: 2px solid #3498db;
    }
    .nav-item {
        display: block;
        padding: 12px 20px;
        margin: 8px 0;
        border-radius: 8px;
        background-color: #f8f9fa;
        color: #2c3e50;
        text-decoration: none;
        transition: background-color 0.2s;
    }
    .nav-item:hover {
        background-color: #e3f2fd;
    }
    .nav-item.active {
        background-color: #3498db;
        color: white !important;
    }
    .nav-icon {
        margin-right: 10px;
        font-size: 18px;
    }
    .logo-container {
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-title">Навигация</div>', unsafe_allow_html=True)

    # Пункты меню
    pages = [
        {"name": "О разработчике", "icon": "👤"},
        {"name": "Информация о датасете", "icon": "📊"},
        {"name": "Визуализации", "icon": "📈"},
        {"name": "Предсказания", "icon": "🔮"}
    ]

    for p in pages:
        is_active = st.session_state.page == p["name"]
        active_class = "active" if is_active else ""

        if st.button(
                f"{p['icon']} {p['name']}",
                key=f"nav_{p['name']}",
                use_container_width=True
        ):
            st.session_state.page = p["name"]

    st.markdown("""
    <div class="logo-container">
        <div style="font-size: 24px;">🤖 Dashboard</div>
        <div style="font-size: 12px; color: #7f8c8d;">v2.1</div>
    </div>
    """, unsafe_allow_html=True)

# Страница 1: О разработчике
if st.session_state.page == "О разработчике":
    # Стили
    st.markdown("""
    <style>
    .developer-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .header-section {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .info-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        margin: 15px 0;
    }
    .section-title {
        color: #2c3e50;
        border-left: 5px solid #3498db;
        padding-left: 15px;
        margin: 25px 0 15px 0;
    }
    .badge {
        display: inline-block;
        background: #3498db;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        margin: 5px 5px 5px 0;
        font-size: 14px;
    }
    .tech-stack {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 20px 0;
    }
    .tech-item {
        text-align: center;
        width: 80px;
        margin: 10px;
    }
    .tech-icon {
        font-size: 36px;
        margin-bottom: 10px;
        color: #4b6cb7;
    }
    .contact-btn {
        background: linear-gradient(to right, #3498db, #2c3e50);
        color: white !important;
        padding: 10px 20px;
        border-radius: 30px;
        text-align: center;
        display: block;
        margin: 20px auto;
        width: 80%;
        text-decoration: none;
        font-weight: bold;
        transition: transform 0.3s;
    }
    .contact-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 14px rgba(0,0,0,0.1);
        text-decoration: none;
        color: white;
    }
    /* Добавленные стили для увеличения расстояния между колонками */
    .st-emotion-cache-keje6w {
        gap: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Шапка
    st.markdown("""
    <div class="header-section">
        <h1>О разработчике проекта</h1>
        <p>Информация о создателе этого дашборда</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Фотка
        try:
            img = Image.open("assets/matr.jpg")
            st.image(img, width=280, use_container_width=True)
        except:
            st.warning("Фото разработчика не найдено")

        st.markdown("""
        <div class="developer-card">
            <h3 style="color: #2c3e50; margin-top: 20px; text-align: center;">Матросова Раиса Евгеньевна</h3>
            <div style="background: #ffffff; padding: 10px; border-radius: 10px; margin: 15px 0; text-align: center;">
                <p style="margin: 0;">ФИТ-232</p>
            </div>
        
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="background: #ffffff; padding: 10px; border-radius: 10px; margin: 15px 0; text-align: center;">
                <h4>👩‍💻 Контакты</h4>
                <p>✉️ matrosova-05@list.ru</p>
                <p>📱 @rmatroskin</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


    with col2:
        st.markdown("""
        <h3 class="section-title">О проекте</h3>
        <h4>📚 Дисциплина</h4>
        <p>МАШИННОЕ ОБУЧЕНИЕ И БОЛЬШИЕ ДАННЫЕ</p>
        <h4 style="margin-top: 20px;">🎯 Тема РГР</h4>
        <p>"Разработка Web-приложения (дашборда) для инференса (вывода) моделей ML и анализа данных"</p>

        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 class="section-title">Стек технологий</h3>
        <div class="info-card">
            <div class="tech-stack">
                <div class="tech-item">
                    <div class="tech-icon">🐍</div>
                    <div>Python</div>
                </div>
                <div class="tech-item">
                    <div class="tech-icon">📊</div>
                    <div>Streamlit</div>
                </div>
                <div class="tech-item">
                    <div class="tech-icon">🤖</div>
                    <div>Scikit-learn</div>
                </div>
                <div class="tech-item">
                    <div class="tech-icon">🧠</div>
                    <div>TensorFlow</div>
                </div>
                <div class="tech-item">
                    <div class="tech-icon">🐱</div>
                    <div>CatBoost</div>
                </div>
                <div class="tech-item">
                    <div class="tech-icon">📈</div>
                    <div>Pandas</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 class="section-title">Ключевые особенности проекта</h3>
        <div class="info-card">
            <div style="display: flex; flex-wrap: wrap;">
                <span class="badge">Визуализации</span>
                <span class="badge">Машинное обучение</span>
                <span class="badge">Анализ данных</span>
                <span class="badge">Предобработка данных</span>
                <span class="badge">Разработка дашборда</span>
                <span class="badge">Нейронные сети</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 class="section-title">Образование</h3>
        <div class="info-card">
            <div style="display: flex; margin-bottom: 20px;">
                <div style="flex: 1; padding-right: 15px;">
                    <h4>🎓 Образование</h4>
                    <p>Омский государственный технический университет</p>
                    <p>ФИТиКС</p>
                    <p>Бакалавриат, 2 курс</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Страница 2: Информация о датасете
elif st.session_state.page == "Информация о датасете":
    st.title("📊 Анализ набора данных Smoke Detection")
    st.markdown("---")

    # Стили
    st.markdown("""
    <style>
    .feature-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .section-title {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    .metric-box {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .feature-table {
        width: 100%;
        border-collapse: collapse;
    }
    .feature-table th {
        background-color: #3498db;
        color: white;
        padding: 12px;
        text-align: left;
    }
    .feature-table td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    .feature-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .tab-content {
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 0 0 10px 10px;
        border-top: none;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-box">
            <h4>Размер набора данных</h4>
            <h3>62,630 записей</h3>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-box">
            <h4>Количество признаков</h4>
            <h3>12 характеристик</h3>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-box">
            <h4>Целевая переменная</h4>
            <h3>Fire Alarm (0/1)</h3>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Ввкладки
    tab1, tab2, tab3 = st.tabs(["📋 Описание данных", "🔍 Примеры данных", "⚙️ Предобработка"])

    with tab1:
        col_context, col_photo = st.columns([2, 1])

        with col_context:
            st.markdown('<h3 class="section-title">Прикладная область</h3>', unsafe_allow_html=True)
            st.markdown("""
            <div class="feature-card">
                <p><strong>Детектор дыма</strong> — устройство для автоматического обнаружения признаков пожара 
                по наличию дыма в воздухе. Современные детекторы используют комбинацию технологий:</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class="feature-card">
                    <h4>📸 Фотоэлектрический</h4>
                    <ul>
                        <li>Использует световой луч</li>
                        <li>Обнаруживает видимые частицы</li>
                        <li>Эффективен для тлеющих пожаров</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="feature-card">
                    <h4>⚡ Ионизационный</h4>
                    <ul>
                        <li>Радиоактивный материал</li>
                        <li>Обнаруживает невидимые частицы</li>
                        <li>Быстро реагирует на пламя</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('<h3 class="section-title">Описание признаков</h3>', unsafe_allow_html=True)
            st.markdown("""
            <div class="feature-card">
                <table class="feature-table">
                    <thead>
                        <tr>
                            <th>Признак</th>
                            <th>Описание</th>
                            <th>Единицы измерения</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>UTC</td><td>Время измерения</td><td>ISO 8601</td></tr>
                        <tr><td>Temperature</td><td>Температура окружающей среды</td><td>°C</td></tr>
                        <tr><td>Humidity</td><td>Относительная влажность</td><td>%</td></tr>
                        <tr><td>TVOC</td><td>Летучие органические соединения</td><td>ppb</td></tr>
                        <tr><td>eCO2</td><td>Эквивалент CO2</td><td>ppm</td></tr>
                        <tr><td>Raw H2</td><td>Сырые показания водорода</td><td>усл.ед.</td></tr>
                        <tr><td>Raw Ethanol</td><td>Сырые показания этанола</td><td>усл.ед.</td></tr>
                        <tr><td>Pressure</td><td>Атмосферное давление</td><td>гПа</td></tr>
                        <tr><td>PM1.0</td><td>Частицы &lt;1.0 мкм</td><td>мкг/м³</td></tr>
                        <tr><td>PM2.5</td><td>Частицы &lt;2.5 мкм</td><td>мкг/м³</td></tr>
                        <tr><td>NC0.5</td><td>Концентрация частиц &lt;0.5 мкм</td><td>#/см³</td></tr>
                        <tr><td>CNT</td><td>Счетчик пожара</td><td>числовой</td></tr>
                        <tr><td>Fire Alarm</td><td>Индикатор пожара</td><td>0/1 бинарный</td></tr>
                    </tbody>
                </table>
            </div>
            """, unsafe_allow_html=True)

        with col_photo:
            try:
                img = Image.open("assets/detector.jpeg")
                st.image(img, caption="Современный комбинированный детектор дыма", use_container_width=True)
            except:
                st.warning("Изображение детектора не найдено")

            st.markdown("""
            <div style="background-color: #e3f2fd; padding: 15px; border-radius: 10px; margin-top: 20px;">
                <h4>🔬 Технические особенности</h4>
                <p>Датчики в детекторах измеряют:</p>
                <ul>
                    <li>Концентрацию частиц разных размеров</li>
                    <li>Концентрацию газов (CO2, TVOC)</li>
                    <li>Температуру и влажность</li>
                    <li>Атмосферное давление</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<h3 class="section-title">Исходные данные</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <p><strong>10 строк первоначального набора данных:</strong></p>
        </div>
        """, unsafe_allow_html=True)

        try:
            df = pd.read_csv(r'C:\Users\Zver\Desktop\ML\data\smoke_detector_task.csv', encoding='utf-8', sep=',')
            st.dataframe(
                df.sample(10),
                use_container_width=True,
                height=300
            )
        except Exception as e:
            st.error(f"Ошибка загрузки данных: {str(e)}")

        st.markdown('<h3 class="section-title" style="margin-top: 30px;">Очищенные данные</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <p><strong>После предобработки и очистки:</strong></p>
        </div>
        """, unsafe_allow_html=True)

        try:
            df_clean = pd.read_csv(r'C:\Users\Zver\Desktop\ML\data\smoke_detector_task_filtered.csv', encoding='utf-8',
                                   sep=',')
            st.dataframe(
                df_clean.sample(10),
                use_container_width=True,
                height=300
            )
        except Exception as e:
            st.error(f"Ошибка загрузки данных: {str(e)}")

    with tab3:
        st.markdown('<h3 class="section-title">Этапы предобработки данных</h3>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <h4>🔎 Первоначальный анализ</h4>
                <ul>
                    <li>Типы данных: float64(11), int64(3), object(1)</li>
                    <li>62630 строк, 15 столбцов</li>
                    <li>Выбросы в TVOC, eCO2, PM1.0, PM2.5</li>
                    <li>Пропуски в большинстве столбцов</li>
                </ul>
            </div>

            <div class="feature-card">
                <h4>🧹 Очистка данных</h4>
                <ul>
                    <li>Заполнение пропусков медианой для:
                        <ul>
                            <li>Temperature[C]</li>
                            <li>TVOC[ppb]</li>
                            <li>eCO2[ppm]</li>
                            <li>Raw H2</li>
                        </ul>
                    </li>
                    <li>Заполнение пропусков средним для:
                        <ul>
                            <li>Humidity[%]</li>
                            <li>Pressure[hPa]</li>
                        </ul>
                    </li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <h4>🔧 Преобразование данных</h4>
                <ul>
                    <li>Изменение типов данных:
                        <ul>
                            <li>'TVOC[ppb]' → int</li>
                            <li>'eCO2[ppm]' → int</li>
                            <li>'Raw H2' → int</li>
                        </ul>
                    </li>
                    <li>Проверка дубликатов:
                        <ul>
                            <li>Дубликаты не обнаружены</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="feature-card">
                <h4>⚖️ Балансировка данных</h4>
                    <ul>
                        <li>Класс 0 (нет пожара): 58,000 записей</li>
                        <li>Класс 1 (пожар): 4,630 записей</li>
                        <li>Применена техника SMOTE для балансировки классов</li>
                        <li>Итоговое соотношение: 1:1</li>
                    </ul>
            </div>
            """, unsafe_allow_html=True)

# Страница 3: Визуализации
elif st.session_state.page == "Визуализации":
    st.title("📊 Анализ данных через визуализации")

    # Стили
    st.markdown("""
    <style>
    .viz-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
    }
    .section-header {
        font-size: 24px;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin: 30px 0 20px 0;
        font-weight: 600;
    }
    .caption-box {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 12px;
        margin-top: 10px;
        text-align: center;
        font-size: 14px;
        color: #5f6c7b;
    }
    </style>
    """, unsafe_allow_html=True)

    # Секция 1: Распределения
    st.markdown('<div class="section-header">Распределения признаков</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    with cols[0]:

        st.image("assets/1.1.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.1: Распределение температуры</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


        st.image("assets/1.2.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.2: Распределение влажности</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[1]:

        st.image("assets/1.3.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.3: Распределение Raw H2</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


        st.image("assets/1.4.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.4: Распределение Raw Ethanol</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[2]:

        st.image("assets/1.5.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.5: Распределение количества газов</div>',
                    unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


        st.image("assets/1.6.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 1.6: Распределение давления</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Секция 2: Диаграммы рассеяния
    st.markdown('<div class="section-header">Диаграммы рассеяния</div>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:

        st.image("assets/2.1.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 2.1: TVOC vs eCO2</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[1]:

        st.image("assets/2.2.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 2.2: Влажность vs H2</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Секция 3: Анализ переменных
    st.markdown('<div class="section-header">Анализ целевой переменной</div>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:

        st.image("assets/3.1.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 3.1: Соотношение срабатываний</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[1]:

        st.image("assets/4.1.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 4.1: Концентрации частиц</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Секция 4: Корреляционный анализ
    st.markdown('<div class="section-header">Корреляционный анализ</div>', unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:

        st.image("assets/5.1.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 5.1: Матрица корреляций (Пожар)</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[1]:

        st.image("assets/5.2.png", use_container_width=True)
        st.markdown('<div class="caption-box">Рисунок 5.2: Матрица корреляций (Нет пожара)</div>',
                    unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Страница 4: Предсказания
elif st.session_state.page == "Предсказания":
    st.title("🔥 Предсказание срабатывания пожарной сигнализации")

    # Стили
    st.markdown("""
    <style>
    .model-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .model-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }
    .model-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
    }
    .model-name {
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
    }
    .close-btn {
        background: #ff6b6b;
        color: white;
        border: none;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        font-size: 14px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .models-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    .prediction-chart {
        margin-top: 20px;
        padding: 15px;
        border-radius: 10px;
        background: #f9f9f9;
    }
    .prediction-container {
        text-align: center;
        margin: 15px 0;
    }
    .prediction-alert {
        border-radius: 8px;
        padding: 15px;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 15px;
    }
    .fire-alert {
        background-color: #ff4b4b30;
        border: 2px solid #ff4b4b;
        color: #d63031;
    }
    .no-fire-alert {
        background-color: #2ecc7130;
        border: 2px solid #2ecc71;
        color: #27ae60;
    }
    .probability-container {
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
    }
    .probability-box {
        text-align: center;
        width: 48%;
    }
    .fire-probability {
        color: #e74c3c;
    }
    .no-fire-probability {
        color: #2ecc71;
    }
    .progress-bar-container {
        margin-top: 15px;
    }
    .progress-bar {
        height: 20px;
        background: #f0f0f0;
        border-radius: 10px;
        overflow: hidden;
    }
    .progress-bar-fill {
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    import pickle
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import numpy as np
    from joblib import load
    import plotly.express as px


    @st.cache_resource
    def load_models():
        models = {
            "KNN": load("C:/Users/Zver/Desktop/machine_learning/notebook/models/knn_model.pkl"),
            "Gradient Boosting": load('C:/Users/Zver/Desktop/machine_learning/notebook/models/gb_model.pkl'),
            "CatBoost": CatBoostClassifier().load_model(
                "C:/Users/Zver/Desktop/machine_learning/notebook/models/catboost_model.cbm"),
            "Bagging": load('C:/Users/Zver/Desktop/machine_learning/notebook/models/bagging_model.pkl'),
            "Stacking": load('C:/Users/Zver/Desktop/machine_learning/notebook/models/stacking_model.pkl'),
            "Optuna Neural Network": tf.keras.models.load_model(
                r"C:\Users\Zver\Desktop\machine_learning\notebook\models\optuna_classification_model.h5")
        }
        return models


    @st.cache_resource
    def load_nn_preprocessors():
        scaler = load(r"C:\Users\Zver\Desktop\machine_learning\notebook\models\nn_scaler.pkl")
        pca = load(r"C:\Users\Zver\Desktop\machine_learning\notebook\models\nn_pca.pkl")
        return scaler, pca


    try:
        models = load_models()
    except Exception as e:
        st.error(f"Ошибка загрузки моделей: {e}")
        st.stop()


    # Валидация
    def validate_input(df):
        validation_rules = {
            'TVOC[ppb]': {'min': 0, 'max': 60000, 'allow_zero': True},
            'eCO2[ppm]': {'min': 200, 'max': 60000, 'allow_zero': False},
            'Temperature[C]': {'min': -50, 'max': 1000, 'allow_zero': True},
            'PM2.5': {'min': 0, 'max': 1000, 'allow_zero': False},
            'NC2.5': {'min': 0, 'max': 1000, 'allow_zero': False},
            'Humidity[%]': {'min': 0, 'max': 100, 'allow_zero': True},
            'PM1.0': {'min': 0, 'max': 1000, 'allow_zero': False},
            'NC0.5': {'min': 0, 'max': 1000, 'allow_zero': False},
            'NC1.0': {'min': 0, 'max': 1000, 'allow_zero': False},
        }

        errors = []
        for idx, row in df.iterrows():
            for feature, rules in validation_rules.items():
                value = row[feature]
                min_val = rules['min']
                max_val = rules['max']
                allow_zero = rules['allow_zero']

                if not (min_val <= value <= max_val):
                    errors.append(f"Строка {idx + 1}: {feature} должен быть между {min_val} и {max_val}")
                if not allow_zero and value <= 0:
                    errors.append(f"Строка {idx + 1}: {feature} должен быть больше 0")
        return errors


    st.header("Выбор моделей")

    # Инициализация состояния для выбранных моделей
    if 'selected_models' not in st.session_state:
        st.session_state.selected_models = list(models.keys())


    # Функция для удаления модели из выбранных
    def remove_model(model_name):
        if model_name in st.session_state.selected_models:
            st.session_state.selected_models.remove(model_name)
            st.rerun()


    # Отображение выбранных моделей с кнопками удаления
    if st.session_state.selected_models:
        st.markdown("**Выбранные модели:**")
        cols = st.columns(4)
        col_idx = 0

        for model_name in st.session_state.selected_models:
            with cols[col_idx]:
                with st.container():
                    st.markdown(f"""
                    <div class="model-card">
                        <div class="model-header">
                            <div class="model-name">{model_name}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("×", key=f"remove_{model_name}", help="Удалить модель"):
                        remove_model(model_name)
            col_idx = (col_idx + 1) % 4

    # Кнопка для выбора всех моделей
    if st.button("Выбрать все модели", use_container_width=True):
        st.session_state.selected_models = list(models.keys())
        st.rerun()

    input_method = st.radio(
        "Выберите способ ввода данных:",
        ["Ввести данные вручную", "Загрузить CSV файл"],
        horizontal=True,
        index=0
    )

    required_columns = [
        'TVOC[ppb]', 'eCO2[ppm]', 'Temperature[C]', 'PM2.5', 'NC2.5',
        'Humidity[%]', 'Raw H2', 'Raw Ethanol', 'Pressure[hPa]',
        'PM1.0', 'NC0.5', 'NC1.0'
    ]

    input_df = pd.DataFrame()
    full_predictions = None

    if input_method == "Ввести данные вручную":
        st.header("Параметры датчиков")

        col1, col2, col3 = st.columns(3)

        with col1:
            temperature = st.number_input("Температура (°C)", min_value=-50.0, max_value=100.0, value=20.0)
            humidity = st.number_input("Влажность (%)", min_value=0.0, max_value=100.0, value=50.0)
            tvoc = st.number_input("TVOC (ppb)", min_value=0, max_value=60000, value=500)
            eco2 = st.number_input("eCO2 (ppm)", min_value=400, max_value=60000, value=1000)

        with col2:
            raw_h2 = st.number_input("Raw H2", min_value=1, max_value=60000, value=10000)
            raw_ethanol = st.number_input("Raw Ethanol", min_value=1, max_value=60000, value=20000)
            pressure = st.number_input("Давление (гПа)", min_value=800.0, max_value=1200.0, value=1013.25)
            pm25 = st.number_input("PM2.5 (мкг/м³)", min_value=0.1, max_value=1000.0, value=10.0)

        with col3:
            pm10 = st.number_input("PM1.0 (мкг/м³)", min_value=0.1, max_value=1000.0, value=5.0)
            nc25 = st.number_input("NC2.5 (#/см³)", min_value=0.1, max_value=1000.0, value=20.0)
            nc05 = st.number_input("NC0.5 (#/см³)", min_value=0.1, max_value=1000.0, value=50.0)
            nc10 = st.number_input("NC1.0 (#/см³)", min_value=0.1, max_value=1000.0, value=30.0)

        input_data = {
            'TVOC[ppb]': [tvoc],
            'eCO2[ppm]': [eco2],
            'Temperature[C]': [temperature],
            'PM2.5': [pm25],
            'NC2.5': [nc25],
            'Humidity[%]': [humidity],
            'Raw H2': [raw_h2],
            'Raw Ethanol': [raw_ethanol],
            'Pressure[hPa]': [pressure],
            'PM1.0': [pm10],
            'NC0.5': [nc05],
            'NC1.0': [nc10]
        }
        input_df = pd.DataFrame(input_data)

    else:
        st.header("Загрузка данных")
        uploaded_file = st.file_uploader("Загрузите CSV файл с данными", type=["csv"])

        if uploaded_file is not None:
            try:
                input_df = pd.read_csv(uploaded_file)
                st.success("Файл успешно загружен!")
                st.write(f"Загружено строк: {len(input_df)}")

                # Удаление целевой переменной, если она присутствует
                if 'Fire Alarm' in input_df.columns:
                    input_df = input_df.drop(columns=['Fire Alarm'])
                    st.info("Целевая переменная 'Fire Alarm' удалена из данных")

                missing_cols = [col for col in required_columns if col not in input_df.columns]
                if missing_cols:
                    st.error(f"Отсутствуют необходимые колонки: {', '.join(missing_cols)}")
                    st.stop()

                # Показ предварительного просмотра
                st.subheader("Предварительный просмотр данных")
                st.dataframe(input_df.head(3))

            except Exception as e:
                st.error(f"Ошибка при чтении файла: {e}")


    # Функция для выполнения предсказаний
    def make_predictions(input_data, models_to_use):
        results = {}

        for model_name in models_to_use:
            try:
                model = models[model_name]
                input_data_for_pred = input_data[required_columns]

                if model_name == "Optuna Neural Network":
                    scaler, pca = load_nn_preprocessors()
                    scaled_data = scaler.transform(input_data_for_pred)
                    pca_data = pca.transform(scaled_data)
                    input_array = pca_data.astype('float32')
                    prediction_proba = model.predict(input_array)
                    predictions = (prediction_proba > 0.5).astype(int).flatten()
                else:
                    predictions = model.predict(input_data_for_pred)
                    if hasattr(model, "predict_proba"):
                        prediction_proba = model.predict_proba(input_data_for_pred)
                    else:
                        # Для моделей без predict_proba
                        prediction_proba = np.zeros((len(predictions), 2))
                        for i, pred in enumerate(predictions):
                            prediction_proba[i, pred] = 1.0

                # Сохраняем результаты
                if model_name == "Optuna Neural Network":
                    fire_probs = prediction_proba[:, 0] if prediction_proba.shape[1] == 1 else prediction_proba[:, 1]
                else:
                    fire_probs = prediction_proba[:, 1]

                results[model_name] = {
                    'predictions': predictions,
                    'fire_probs': fire_probs,
                    'no_fire_probs': 1 - fire_probs
                }

            except Exception as e:
                st.error(f"Ошибка предсказания для модели {model_name}: {str(e)}")

        return results


    # Обработка кнопки предсказания
    if st.button("Выполнить предсказания", use_container_width=True, type="primary") and not input_df.empty:
        if not st.session_state.selected_models:
            st.warning("Пожалуйста, выберите хотя бы одну модель")
            st.stop()

        try:
            errors = validate_input(input_df)
            if errors:
                st.error("Обнаружены ошибки в данных:")
                for error in errors:
                    st.error(error)
                st.stop()

            with st.spinner('Выполняем предсказания... Это может занять несколько минут'):
                results = make_predictions(input_df, st.session_state.selected_models)

                if input_method == "Ввести данные вручную":
                    st.markdown("## Результаты предсказаний")

                    # Создаем данные для графика
                    model_names = []
                    fire_probs = []
                    no_fire_probs = []

                    for model_name, result in results.items():
                        prediction = result['predictions'][0]
                        fire_prob = result['fire_probs'][0] * 100
                        no_fire_prob = result['no_fire_probs'][0] * 100

                        model_names.append(model_name)
                        fire_probs.append(fire_prob)
                        no_fire_probs.append(no_fire_prob)

                        # Отображение карточки с предсказанием
                        with st.container():
                            st.markdown(f"""
                            <div class="model-card">
                                <div class="model-header">
                                    <div class="model-name">{model_name}</div>
                                </div>

                                <div class="prediction-container">
                                    <div class="prediction-alert {'fire-alert' if prediction == 1 else 'no-fire-alert'}">
                                        {'ПОЖАР!' if prediction == 1 else 'Нет пожара'}
                                    </div>
                                </div>

                                <div class="probability-container">
                                    <div class="probability-box">
                                        <div style="font-weight: bold;" class="fire-probability">Вероятность пожара</div>
                                        <div style="font-size: 24px; font-weight: bold;" class="fire-probability">
                                            {fire_prob:.2f}%
                                        </div>
                                    </div>
                                    <div class="probability-box">
                                        <div style="font-weight: bold;" class="no-fire-probability">Вероятность отсутствия</div>
                                        <div style="font-size: 24px; font-weight: bold;" class="no-fire-probability">
                                            {no_fire_prob:.2f}%
                                        </div>
                                    </div>
                                </div>

                                <div class="progress-bar-container">
                                    <div class="progress-bar">
                                        <div class="progress-bar-fill" style="width: {fire_prob}%; background: #e74c3c;"></div>
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                    # Визуализация результатов всех моделей на одном графике
                    st.markdown("## Сравнение результатов моделей")

                    # Создаем DataFrame для графика
                    df_plot = pd.DataFrame({
                        'Модель': model_names,
                        'Вероятность пожара (%)': fire_probs,
                        'Вероятность отсутствия (%)': no_fire_probs
                    })

                    # Преобразуем данные для Plotly
                    df_melted = df_plot.melt(id_vars='Модель',
                                             value_vars=['Вероятность пожара (%)', 'Вероятность отсутствия (%)'],
                                             var_name='Тип вероятности',
                                             value_name='Процент')

                    # Создаем интерактивный график
                    fig = px.bar(df_melted,
                                 x='Модель',
                                 y='Процент',
                                 color='Тип вероятности',
                                 barmode='group',
                                 color_discrete_map={
                                     'Вероятность пожара (%)': '#e74c3c',
                                     'Вероятность отсутствия (%)': '#2ecc71'
                                 },
                                 height=500)

                    fig.update_layout(
                        title='Сравнение вероятностей предсказаний',
                        xaxis_title='Модель',
                        yaxis_title='Вероятность (%)',
                        legend_title='Тип вероятности',
                        hovermode='x'
                    )

                    st.plotly_chart(fig, use_container_width=True)

                else:  # Для загруженного файла
                    result_df = input_df.copy()

                    for model_name, result in results.items():
                        result_df[f'{model_name}_prediction'] = result['predictions']
                        result_df[f'{model_name}_fire_prob'] = result['fire_probs']
                        result_df[f'{model_name}_no_fire_prob'] = result['no_fire_probs']

                    st.success("Предсказания успешно выполнены!")
                    st.write(f"Всего записей: {len(result_df)}")

                    # Показ первых 10 строк
                    st.subheader("Первые 10 предсказаний")
                    st.dataframe(result_df.head(10))

                    # Визуализация распределения предсказаний
                    st.subheader("Распределение предсказаний")

                    # Создаем DataFrame для визуализации
                    prediction_counts = {}
                    for model_name in st.session_state.selected_models:
                        counts = result_df[f'{model_name}_prediction'].value_counts().to_dict()
                        prediction_counts[model_name] = {
                            'Пожар': counts.get(1, 0),
                            'Нет пожара': counts.get(0, 0)
                        }

                    df_counts = pd.DataFrame(prediction_counts).T.reset_index()
                    df_counts = df_counts.rename(columns={'index': 'Модель'})
                    df_melted = df_counts.melt(id_vars='Модель',
                                               value_vars=['Пожар', 'Нет пожара'],
                                               var_name='Предсказание',
                                               value_name='Количество')

                    # Создаем интерактивный график
                    fig = px.bar(df_melted,
                                 x='Модель',
                                 y='Количество',
                                 color='Предсказание',
                                 barmode='group',
                                 color_discrete_map={
                                     'Пожар': '#e74c3c',
                                     'Нет пожара': '#2ecc71'
                                 },
                                 height=500)

                    fig.update_layout(
                        title='Количество предсказаний по моделям',
                        xaxis_title='Модель',
                        yaxis_title='Количество предсказаний',
                        legend_title='Тип предсказания',
                        hovermode='x'
                    )

                    st.plotly_chart(fig, use_container_width=True)

                    # Кнопка для скачивания полных результатов
                    csv = result_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Скачать все предсказания (CSV)",
                        data=csv,
                        file_name='predictions_results.csv',
                        mime='text/csv',
                        use_container_width=True
                    )

        except Exception as e:
            st.error(f"Ошибка выполнения предсказаний: {str(e)}")
    elif input_df.empty:
        st.warning("Пожалуйста, введите данные для выполнения предсказания")
# streamlit run app.py

