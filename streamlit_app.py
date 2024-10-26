import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="تحليل سوق العمل: أسئلة وجاوبناها", layout="centered")

st.markdown(
    """
    <style>
    body{
        text-align: right; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("تحليل سوق العمل: الأسئلة والإجابات")
st.write("هنا بنستعرض الأسئلة اللي واجهتنا في تحليل بيانات الوظائف، ونشوف كيف جاوبنا عليها")

# Load the data
df = pd.read_csv('cleaned_data.csv')

# Question 1
st.header("السؤال 1️⃣: ما نسبة الوظائف لكل منطقة في المملكة؟")
st.write("أول سؤال كان عن توزيع الوظائف في كل منطقة. يعني نبغى نعرف وين بالضبط يتركز الطلب على التوظيف. طلع معانا إنه في بعض المناطق عندها نسبة كبيرة من الفرص، زي ما تشوفون في الرسم البياني، بينما بعض المناطق الفرص فيها أقل شوي. هذا يعطينا صورة عن تركز الوظائف في أماكن معينة أكثر من غيرها")

region_counts = df['region'].value_counts(normalize=True) * 100
fig = px.bar(region_counts, x=region_counts.index, y=region_counts.values, labels={'x': "المنطقة", 'y': "النسبة %"})
fig.update_layout(title="نسبة الوظائف في مناطق المملكة", title_x=0.45)
st.plotly_chart(fig)

# Question 2
st.header("السؤال 2️⃣: نسبة توزيع الذكور و الإناث في الوظائف؟")
st.write("السؤال الثاني كان بخصوص نسبة الذكور إلى الإناث في الوظائف. هل في تفضيل معين للجنس؟ ولا الكل عنده فرص متساوية؟ طلع معنا إنه فيه توازن نسبي، ولكن كمان فيه وظائف مخصصة للجنسين وأخرى مفضلة لجنس معين. هنا أضفنا رسم بياني يوضح النسب بشكل حلو وسهل")

gender_mapping = {'Female': 'إناث', 'Male': 'ذكور', 'Both': 'كليهما'}
df['gender'] = df['gender'].map(gender_mapping)

gender_counts = df['gender'].value_counts()
fig = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index, labels={'label': "الجنس", 'value': "النسبة %"})
fig.update_layout(title="توزيع الجنس في الوظائف", title_x=0.45)
st.plotly_chart(fig)

# Question 3
st.header("السؤال 3️⃣: ما نطاق الرواتب المتوقع للخريجين الجدد؟")
st.write("أما عن الرواتب، فسؤالنا كان عن الرواتب اللي ممكن يتوقعها الخريج الجديد. جبنا الداتا وطلعنا منها رسم بياني يوضح توزيع الرواتب. واضح إن الأغلب يحصل على راتب متوسط، بس فيه شريحة تستلم رواتب أعلى شوي. هذا مهم عشان يعرف الخريج اللي داخل السوق وش يتوقع")

fig = px.histogram(df, x='salary', nbins=30, labels={'salary': "الراتب"})
fig.update_layout(title="توزيع رواتب الخريجين الجدد", title_x=0.45)
st.plotly_chart(fig)

# Question 4
st.header("السؤال 4️⃣: هل تستهدف الوظائف ذوي الخبرة أم الخريجين الجدد؟")
st.write("الرسم يوضح توازن في الفرص بين الخريجين الجدد وأصحاب الخبرة البسيطة. فيه وظائف كثيرة ما تتطلب خبرة، وهذا ممتاز للخريجين الجدد. وبنفس الوقت، فيه فرص لأصحاب الخبرة البسيطة (سنتين مثلاً). يعني السوق فيه مجال للجميع، سواء كنت جديد أو عندك خبرة بسيطة")

experience_counts = df['exper'].value_counts()
fig = px.bar(experience_counts, x=experience_counts.index, y=experience_counts.values, labels={'x': "مستوى الخبرة", 'y': "عدد الوظائف"})
fig.update_layout(title="توزيع الخبرة المطلوبة", title_x=0.45)
st.plotly_chart(fig)

# Question 5
st.header("السؤال 5️⃣: ما هي الوظائف الأكثر طلباً في سوق العمل؟")
st.write("هذا السؤال بيخلينا نعرف أكثر عن نوعية الوظائف اللي عليها إقبال كبير ونشوف وش المجالات اللي سوق العمل يطلبها بكثرة")

# Calculate the most in-demand job titles
job_title_counts = df['job_title'].value_counts().head(10)  # Top 10 most frequent job titles

# Plot the chart
fig = px.bar(job_title_counts, x=job_title_counts.index, y=job_title_counts.values,
             labels={'x': "الوظيفة", 'y': "عدد الوظائف"})
fig.update_layout(title="الوظائف الأكثر طلباً في سوق العمل", title_x=0.45)

# Display the chart
st.plotly_chart(fig)


# End of analysis
st.header("📌 نهاية التحليل")
st.write("و بكذا خلصنا استعراض أبرز الأسئلة اللي واجهتنا في تحليل سوق العمل السعودي. إن شاء الله تكونوا استفدتوا من هالمعلومات، وحنكون معكم دايمًا لأي استفسار ثاني")
