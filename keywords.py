
# ============================================================
# 1. JOB_KEYWORDS
# ============================================================
# Indican que alguien está buscando/contratando a una persona.
# Incluye inglés + español y muchas variantes.

JOB_KEYWORDS = [
    # Inglés - hiring
    "hiring",
    "we're hiring",
    "were hiring",
    "we are hiring",
    "now hiring",
    "currently hiring",
    "actively hiring",
    "looking to hire",
    "looking to hire an editor",
    "looking to hire a video editor",
    "looking for an editor",
    "looking for a video editor",
    "looking for editors",
    "looking for video editors",
    "looking for a freelance editor",
    "looking for freelance editors",
    "seeking an editor",
    "seeking a video editor",
    "seeking editors",
    "seeking video editors",
    "seeking a freelance editor",
    "need an editor",
    "need a video editor",
    "need editors",
    "need video editors",
    "need someone to edit",
    "need someone to edit videos",
    "need someone for video editing",
    "editor needed",
    "video editor needed",
    "editors needed",
    "video editors needed",
    "editor wanted",
    "video editor wanted",
    "editors wanted",
    "video editors wanted",
    "wanted video editor",
    "wanted editor",
    "we need an editor",
    "we need a video editor",
    "we need editors",
    "we need video editors",
    "i need an editor",
    "i need a video editor",
    "i'm looking for an editor",
    "im looking for an editor",
    "i'm looking for a video editor",
    "im looking for a video editor",
    "i am looking for an editor",
    "i am looking for a video editor",
    "join our team",
    "join the team",
    "join our editing team",
    "join our video team",
    "editor role",
    "video editor role",
    "editing role",
    "video editing role",
    "editor position",
    "video editor position",
    "editing position",
    "open editor position",
    "open video editor position",
    "editor opportunity",
    "video editor opportunity",
    "editing opportunity",
    "editor opening",
    "video editor opening",
    "editing opening",
    "freelance editor needed",
    "freelance video editor needed",
    "freelance editor wanted",
    "freelance video editor wanted",
    "freelance editor",
    "freelance video editor",
    "contract editor",
    "contract video editor",
    "editor contractor",
    "video editor contractor",
    "paid editor",
    "paid video editor",
    "paid editing work",
    "paid editing job",
    "paid video editing",
    "paid opportunity",
    "paid opportunity for editors",

    # Reddit-style hiring titles
    "[hiring]",
    "[hired]",
    "hiring:",
    "hiring -",
    "hiring —",
    "[job]",
    "[jobs]",
    "[paid]",
    "[paid work]",
    "[freelance]",
    "[freelancer wanted]",
    "[editor wanted]",
    "[editor needed]",
    "[video editor wanted]",
    "[video editor needed]",

    # Español
    "busco editor",
    "busco editor de video",
    "busco editor de vídeo",
    "busco editores",
    "busco editores de video",
    "busco editor freelance",
    "busco editor de video freelance",
    "buscamos editor",
    "buscamos editor de video",
    "buscamos editores",
    "buscamos editores de video",
    "se busca editor",
    "se busca editor de video",
    "se buscan editores",
    "se buscan editores de video",
    "necesito editor",
    "necesito editor de video",
    "necesitamos editor",
    "necesitamos editor de video",
    "editor necesario",
    "editor requerido",
    "editor de video requerido",
    "editor solicitado",
    "buscando editor",
    "buscando editor de video",
    "buscando editores",
    "buscando editores de video",
    "buscando un editor",
    "buscando un editor de video",
    "contratando editor",
    "contratando editor de video",
    "contratamos editor",
    "contratamos editor de video",
    "se contrata editor",
    "se contrata editor de video",
    "contrato editor",
    "puesto de editor",
    "puesto de editor de video",
    "vacante editor",
    "vacante editor de video",
    "trabajo de editor",
    "trabajo de edición",
    "trabajo de edición de video",
    "oferta de trabajo",
    "oferta laboral",
    "oferta de editor",
    "oferta para editor",
    "oportunidad para editor",
    "editor freelance buscado",
    "editor freelance requerido",
    "editor de video freelance requerido",
    "editor de video freelance buscado",
]


# ============================================================
# 2. REMOTE_KEYWORDS
# ============================================================

REMOTE_KEYWORDS = [
    # Inglés
    "remote",
    "remote work",
    "remote job",
    "remote position",
    "remote role",
    "remote opportunity",
    "remote worker",
    "remote editor",
    "remote video editor",
    "fully remote",
    "100% remote",
    "completely remote",
    "totally remote",
    "permanently remote",
    "work remotely",
    "working remotely",
    "work from home",
    "working from home",
    "work-from-home",
    "work from anywhere",
    "work anywhere",
    "work from anywhere in the world",
    "anywhere in the world",
    "anywhere worldwide",
    "worldwide",
    "worldwide remote",
    "global remote",
    "location independent",
    "location-independent",
    "no location restriction",
    "no geographic restriction",
    "virtual position",
    "virtual job",
    "virtual work",
    "online position",
    "online job",
    "online work",
    "WFH",
    "wfh",
    "home based",
    "home-based",
    "home based position",
    "home-based position",

    # Español
    "remoto",
    "remota",
    "remotos",
    "remotas",
    "trabajo remoto",
    "trabajo remoto desde casa",
    "empleo remoto",
    "puesto remoto",
    "posición remota",
    "trabajo a distancia",
    "trabajar a distancia",
    "trabajo desde casa",
    "trabajar desde casa",
    "desde casa",
    "100% remoto",
    "completamente remoto",
    "totalmente remoto",
    "remoto al 100%",
    "desde cualquier lugar",
    "desde cualquier parte",
    "desde cualquier lugar del mundo",
    "desde cualquier parte del mundo",
    "sin ubicación",
    "sin restricción geográfica",
    "sin importar ubicación",
    "online",
    "en línea",
    "virtual",
    "teletrabajo",
    "teletrabajar",
    "home office",
]


# ============================================================
# 3. PAY_KEYWORDS
# ============================================================
# Pago en USD o crypto.
#
# OJO:
# Los formatos "$", "usd", etc. pueden generar falsos positivos.
# El bot debería comprobar también que el contexto esté relacionado
# con pago/salario/tarifa antes de aceptar el post.


PAY_KEYWORDS = [
    # USD
    "usd",
    "us$",
    "u.s. dollar",
    "u.s. dollars",
    "us dollars",
    "us dollar",
    "dollar",
    "dollars",
    "in usd",
    "paid in usd",
    "payment in usd",
    "pay in usd",
    "salary in usd",
    "rate in usd",
    "usd payment",
    "usd pay",
    "usd salary",
    "usd/hour",
    "usd/hr",
    "usd/day",
    "usd/week",
    "usd/month",
    "usd/video",
    "usd per hour",
    "usd per day",
    "usd per week",
    "usd per month",
    "usd per video",
    "dollars per hour",
    "dollars per video",
    "dollars per month",
    "paid in dollars",
    "pay in dollars",
    "payment in dollars",

    # Símbolo de dólar + formatos frecuentes
    "$/hour",
    "$/hr",
    "$/day",
    "$/week",
    "$/month",
    "$/video",
    "$ per hour",
    "$ per hr",
    "$ per day",
    "$ per week",
    "$ per month",
    "$ per video",
    "$/edit",
    "$ per edit",
    "$/short",
    "$ per short",
    "$/reel",
    "$ per reel",

    # Crypto
    "crypto",
    "cryptocurrency",
    "crypto payment",
    "crypto payments",
    "paid in crypto",
    "payment in crypto",
    "pay in crypto",
    "crypto pay",
    "cryptocurrency payment",
    "cryptocurrency payments",
    "paid with crypto",

    # USDT
    "usdt",
    "tether",
    "paid in usdt",
    "payment in usdt",
    "pay in usdt",
    "usdt payment",
    "usdt payments",
    "usdt/hour",
    "usdt/hr",
    "usdt/video",
    "usdt per video",

    # USDC
    "usdc",
    "paid in usdc",
    "payment in usdc",
    "pay in usdc",

    # Bitcoin
    "btc",
    "bitcoin",
    "paid in btc",
    "paid in bitcoin",
    "payment in btc",
    "payment in bitcoin",

    # Ethereum
    "eth",
    "ethereum",
    "paid in eth",
    "paid in ethereum",

    # Redes / pagos crypto
    "trc20",
    "erc20",
    "bep20",
    "bsc",
    "binance smart chain",
    "solana",
    "sol",
    "polygon",
    "matic",
    "crypto wallet",
    "wallet address",
    "crypto transfer",

    # Español
    "pago en usd",
    "pago en dólares",
    "pago en dolares",
    "pagado en usd",
    "pagado en dólares",
    "pagado en dolares",
    "pagar en usd",
    "pagar en dólares",
    "salario en usd",
    "tarifa en usd",
    "usd por hora",
    "usd por video",
    "usd al mes",
    "usd por mes",
    "pago en crypto",
    "pago en criptomonedas",
    "pagado en crypto",
    "pagado en criptomonedas",
    "pago en usdt",
    "pagado en usdt",
]


# ============================================================
# 4. SPANISH_INDICATORS
# ============================================================
# Indican que el contenido/audiencia es español o LATAM.
#
# IMPORTANTE:
# Países/nacionalidades son indicadores débiles. Por ejemplo,
# "editor needed for a client in Mexico" no garantiza que el
# contenido esté en español. El bot debería tratarlos con menor
# peso que "Spanish content" o "videos in Spanish".


SPANISH_INDICATORS = [
    # Idioma explícito
    "spanish",
    "spanish-speaking",
    "spanish speaking",
    "spanish language",
    "spanish content",
    "spanish videos",
    "spanish video",
    "spanish youtube",
    "spanish channel",
    "spanish audience",
    "content in spanish",
    "videos in spanish",
    "video in spanish",
    "channel in spanish",
    "audience in spanish",
    "native spanish",
    "native spanish speaker",
    "fluent spanish",
    "castilian",
    "castellano",

    # Español
    "español",
    "espanol",
    "en español",
    "contenido en español",
    "videos en español",
    "video en español",
    "canal en español",
    "audiencia en español",
    "público en español",
    "publico en español",
    "habla español",
    "habla espanol",
    "hispanohablante",
    "hispanohablantes",
    "hablantes de español",
    "audiencia hispana",
    "público hispano",
    "publico hispano",
    "contenido hispano",
    "mercado hispano",
    "español latino",
    "espanol latino",
    "español latinoamericano",
    "espanol latinoamericano",
    "latinoamericano",
    "latinoamericana",

    # LATAM
    "latam",
    "latin america",
    "latin american",
    "latin-america",
    "latin-american",
    "latino",
    "latina",
    "latinos",
    "latinas",
    "latino audience",
    "latina audience",
    "latin audience",
    "latin american audience",
    "latin american market",
    "latam audience",
    "latam market",
    "mercado latino",
    "mercado latinoamericano",
    "audiencia latina",
    "público latino",
    "publico latino",

    # Países
    "argentina",
    "argentinian",
    "argentinian",
    "argentine",
    "mexico",
    "méxico",
    "mexican",
    "colombia",
    "colombian",
    "chile",
    "chilean",
    "peru",
    "peruvian",
    "ecuador",
    "ecuadorian",
    "bolivia",
    "bolivian",
    "paraguay",
    "paraguayan",
    "uruguay",
    "uruguayan",
    "venezuela",
    "venezuelan",
    "guatemala",
    "guatemalan",
    "honduras",
    "honduran",
    "el salvador",
    "salvadoran",
    "nicaragua",
    "nicaraguan",
    "costa rica",
    "costa rican",
    "panama",
    "panamanian",
    "puerto rico",
    "puerto rican",
    "dominican republic",
    "dominican",

    # España
    "spain",
    "spanish spain",
    "españa",
    "españa",
    "español de españa",
    "espanol de espana",
    "spanish from spain",

    # Contenido dirigido a hispanos
    "hispanic",
    "hispanic audience",
    "hispanic market",
    "hispanic content",
    "hispanic community",
    "latino content",
    "latina content",
    "latino creator",
    "latina creator",
    "spanish creator",
    "spanish youtuber",
    "spanish-speaking creator",
]


# ============================================================
# 5. ENGLISH_BASIC_INDICATORS
# ============================================================
# Indicadores de que el contenido puede ser en inglés.
#
# No significa necesariamente que sea "inglés fácil", pero sirve
# como indicador secundario cuando el post menciona explícitamente
# contenido/audio/subtítulos en inglés.


ENGLISH_BASIC_INDICATORS = [
    "english",
    "english content",
    "english videos",
    "english video",
    "english channel",
    "english youtube",
    "english audience",
    "content in english",
    "videos in english",
    "video in english",
    "channel in english",
    "audience in english",
    "english speaking",
    "english-speaking",
    "english speaker",
    "english speaking audience",
    "basic english",
    "simple english",
    "easy english",
    "plain english",
    "english subtitles",
    "english captions",
    "english voiceover",
]


# ============================================================
# 6. VIDEO_EDITING_KEYWORDS
# ============================================================
# Esta lista es MUY importante.
#
# Evita que [Hiring] / [For Hire] haga pasar trabajos de:
# - programación
# - traducción
# - VA
# - soporte
# - ingeniería
# - diseño gráfico puro
# - etc.
#
# El post debería contener al menos uno de estos términos
# (o una coincidencia equivalente) para considerarlo relacionado
# con edición de video.


VIDEO_EDITING_KEYWORDS = [
    # General
    "video editor",
    "video editing",
    "video edit",
    "video edits",
    "editing videos",
    "edit videos",
    "edit video",
    "video editing job",
    "video editing work",
    "video editing position",
    "video editing role",
    "video editing project",
    "editor de video",
    "editor de vídeo",
    "edición de video",
    "edicion de video",
    "edición de vídeo",
    "edicion de video",
    "editar videos",
    "editar vídeos",
    "edición audiovisual",
    "editor audiovisual",

    # Short-form
    "short form editor",
    "short-form editor",
    "short form video editor",
    "short-form video editor",
    "short form editing",
    "short-form editing",
    "shorts editor",
    "youtube shorts editor",
    "shorts editing",
    "tiktok editor",
    "tiktok video editor",
    "tiktok editing",
    "reels editor",
    "instagram reels editor",
    "reels editing",
    "shorts",
    "reels",
    "tiktok videos",

    # Long-form
    "long form editor",
    "long-form editor",
    "long form video editor",
    "long-form video editor",
    "long form editing",
    "youtube editor",
    "youtube video editor",
    "youtube editing",
    "youtube videos",
    "youtube content editor",

    # Social media
    "social media video editor",
    "social media editor",
    "social video editor",
    "social media editing",
    "content editor",
    "video content editor",
    "content video editor",
    "creator editor",
    "creator video editor",
    "youtube creator",
    "content creator editor",

    # Podcasts
    "podcast editor",
    "podcast video editor",
    "podcast editing",
    "video podcast editor",
    "podcast clips",
    "podcast clips editor",
    "podcast shorts",
    "podcast reels",

    # Gaming
    "gaming editor",
    "gaming video editor",
    "gaming video editing",
    "gameplay editor",
    "gaming content editor",
    "youtube gaming editor",

    # Specific formats
    "talking head editor",
    "talking-head editor",
    "talking head video",
    "faceless video editor",
    "faceless videos",
    "faceless youtube",
    "ugc editor",
    "ugc video editor",
    "ugc editing",
    "ad editor",
    "video ad editor",
    "advertisement editor",
    "commercial editor",
    "commercial video editor",
    "promo video editor",
    "promotional video editor",
    "documentary editor",
    "documentary video editor",
    "wedding video editor",
    "real estate video editor",
    "course video editor",
    "educational video editor",
    "fitness video editor",
    "sports video editor",
    "podcast video editor",

    # Motion / effects
    "motion graphics editor",
    "motion graphics",
    "after effects editor",
    "vfx editor",
    "visual effects editor",
    "video effects",
    "transitions",
    "captions",
    "subtitles",
    "video captions",
    "video subtitles",
    "animated captions",
    "kinetic typography",

    # Software específico de edición
    "premiere pro",
    "adobe premiere",
    "premiere",
    "davinci resolve",
    "davinci",
    "resolve editor",
    "final cut pro",
    "final cut",
    "after effects",
    "capcut",
    "filmora",
    "vegas pro",
    "adobe premiere pro",
]


# ============================================================
# 7. EXCLUDE_LEVEL
# ============================================================
# Nivel avanzado que queremos excluir.
#
# NO incluir:
# beginner / junior / entry-level / no experience / intermediate
# porque esos niveles sí nos interesan.


EXCLUDE_LEVEL = [
    # Senior
    "senior",
    "senior editor",
    "senior video editor",
    "senior video editing",
    "senior-level",
    "senior level",
    "sr. editor",
    "sr editor",
    "sr. video editor",
    "lead editor",
    "lead video editor",
    "principal editor",
    "principal video editor",
    "head of editing",
    "head of video",
    "head of video editing",

    # Expert
    "expert",
    "expert editor",
    "expert video editor",
    "expert-level",
    "expert level",
    "expertise required",
    "expert knowledge",
    "expert skills",
    "master editor",
    "mastery required",
    "specialist editor",

    # Advanced
    "advanced",
    "advanced editor",
    "advanced video editor",
    "advanced video editing",
    "advanced editing",
    "advanced skills",
    "advanced skills required",
    "advanced experience",
    "advanced knowledge",

    # Experiencia alta
    "highly experienced",
    "extensively experienced",
    "extensive experience",
    "extensive editing experience",
    "extensive video editing experience",
    "proven extensive experience",
    "years of professional experience",
    "many years of experience",
    "significant experience",

    # Años de experiencia
    "5+ years",
    "5+ years experience",
    "5+ years of experience",
    "6+ years",
    "6+ years experience",
    "6+ years of experience",
    "7+ years",
    "7+ years experience",
    "7+ years of experience",
    "8+ years",
    "8+ years experience",
    "8+ years of experience",
    "10+ years",
    "10+ years experience",
    "10+ years of experience",
    "5 years experience",
    "6 years experience",
    "7 years experience",
    "8 years experience",
    "10 years experience",

    # Profesional avanzado
    "professional editor",
    "professional video editor",
    "top-tier editor",
    "elite editor",
    "high-level editor",
    "high level editor",
    "advanced professional",
    "industry professional",
    "industry veteran",

    # Español
    "senior",
    "editor senior",
    "editor de video senior",
    "nivel senior",
    "nivel avanzado",
    "avanzado",
    "editor experto",
    "experto",
    "experta",
    "experiencia avanzada",
    "experiencia extensa",
    "amplia experiencia",
    "experiencia profesional extensa",
    "más de 5 años",
    "mas de 5 años",
    "más de 6 años",
    "mas de 6 años",
    "más de 7 años",
    "mas de 7 años",
    "más de 8 años",
    "mas de 8 años",
    "más de 10 años",
    "mas de 10 años",
    "5 años de experiencia",
    "6 años de experiencia",
    "7 años de experiencia",
    "8 años de experiencia",
    "10 años de experiencia",
    "editor profesional",
    "editor de video profesional",
]


# ============================================================
# 8. VALID_LEVEL_KEYWORDS
# ============================================================
# No son exclusiones.
# Sirven para detectar ofertas accesibles para nosotros.


VALID_LEVEL_KEYWORDS = [
    "beginner",
    "beginners",
    "beginner friendly",
    "beginner-friendly",
    "entry level",
    "entry-level",
    "entrylevel",
    "junior",
    "junior editor",
    "junior video editor",
    "jr editor",
    "jr. editor",
    "no experience",
    "no prior experience",
    "no experience required",
    "experience not required",
    "training provided",
    "will train",
    "training included",
    "willing to train",
    "new editors",
    "new editor",
    "new to editing",
    "starting out",
    "starting level",
    "intermediate",
    "intermediate editor",
    "intermediate video editor",
    "all experience levels",
    "all skill levels",
    "any experience level",
    "open to beginners",
    "beginners welcome",
    "no previous experience",
    "sin experiencia",
    "sin experiencia previa",
    "no se requiere experiencia",
    "sin experiencia requerida",
    "principiante",
    "principiantes",
    "nivel inicial",
    "nivel principiante",
    "nivel junior",
    "junior",
    "intermedio",
    "nivel intermedio",
    "todos los niveles",
    "todos los niveles de experiencia",
    "se capacita",
    "capacitación incluida",
    "formación incluida",
]


# ============================================================
# 9. EXCLUDE_TOPICS
# ============================================================
# Posts que hablan de edición pero no son ofertas de trabajo.


EXCLUDE_TOPICS = [
    # Tutoriales / aprendizaje
    "tutorial",
    "tutorials",
    "how to",
    "how do i",
    "how can i",
    "how should i",
    "guide",
    "guides",
    "step by step",
    "step-by-step",
    "tips",
    "tip",
    "tricks",
    "how-to",
    "learn",
    "learning",
    "course",
    "courses",
    "class",
    "classes",
    "lesson",
    "lessons",
    "training",
    "workshop",
    "masterclass",

    # Preguntas / ayuda
    "question",
    "questions",
    "question?",
    "help",
    "help me",
    "need help",
    "can someone help",
    "anyone know",
    "does anyone know",
    "what do you think",
    "what should i",
    "is there a way",
    "how much should i",
    "why does",
    "why is",
    "any advice",
    "advice",
    "asking for advice",
    "looking for advice",

    # Reviews / opiniones
    "review",
    "reviews",
    "reviewing",
    "opinion",
    "opinions",
    "thoughts on",
    "what do you think about",
    "first impressions",
    "comparison",
    "compare",
    "vs",
    "versus",
    "alternative to",
    "best software",
    "best editor",
    "best video editor",
    "best editing software",

    # Software / hardware
    "software recommendation",
    "software recommendations",
    "plugin",
    "plugins",
    "preset",
    "presets",
    "template",
    "templates",
    "hardware",
    "gpu",
    "graphics card",
    "cpu",
    "ram",
    "ssd",
    "computer build",
    "pc build",
    "laptop recommendation",
    "monitor recommendation",

    # Comunidad / discusión
    "discussion",
    "discuss",
    "community",
    "showcase",
    "show your work",
    "portfolio",
    "my portfolio",
    "feedback",
    "critique",
    "criticism",
    "roast my",
    "rate my edit",
    "rate my video",
    "check out my",
    "i made this",
    "i edited this",
    "my latest edit",
    "my new video",

    # Noticias / anuncios
    "news",
    "announcement",
    "announced",
    "update",
    "release",
    "released",
    "launch",
    "launched",
    "new version",
    "new update",

    # Precios / carrera
    "how much do editors charge",
    "how much should editors charge",
    "what should i charge",
    "what do you charge",
    "editor rates",
    "editing rates",
    "video editing rates",
    "pricing",
    "pricing advice",
    "career advice",
    "job advice",
    "freelance advice",

    # Educación
    "student",
    "students",
    "homework",
    "assignment",
    "school project",
    "college project",
    "university project",
    "exam",

    # Estafas / legitimidad
    "scam",
    "scammer",
    "scam alert",
    "is this a scam",
    "is this legit",
    "is this legitimate",
    "legit or scam",

    # Español
    "tutorial",
    "cómo hacer",
    "como hacer",
    "cómo puedo",
    "como puedo",
    "ayuda",
    "necesito ayuda",
    "pregunta",
    "preguntas",
    "consejos",
    "recomendación",
    "recomendaciones",
    "reseña",
    "reseñas",
    "opinión",
    "opiniones",
    "comparación",
    "comparar",
    "discusión",
    "debate",
    "feedback",
    "crítica",
    "portafolio",
    "portafolio",
    "noticias",
    "anuncio",
    "actualización",
    "curso",
    "cursos",
    "aprender",
    "aprendiendo",
    "estudiante",
    "tarea",
    "tareas",
    "cuánto cobrar",
    "cuanto cobrar",
    "cuánto cobran los editores",
    "precios",
    "tarifas",
    "consejos laborales",
    "consejos de trabajo",
    "estafa",
    "estafa?",
    "es una estafa",
    "es scam",
]


# ============================================================
# 10. NON_VIDEO_JOB_KEYWORDS
# ============================================================
# Trabajos que suelen aparecer junto a [Hiring] / [For Hire],
# pero NO son edición de video.
#
# Esta lista es especialmente útil para limpiar los resultados
# que mostraste en el ejemplo.


NON_VIDEO_JOB_KEYWORDS = [
    # Programming / software
    "developer",
    "software developer",
    "web developer",
    "frontend developer",
    "front-end developer",
    "backend developer",
    "back-end developer",
    "full-stack developer",
    "full stack developer",
    "software engineer",
    "web engineer",
    "frontend engineer",
    "backend engineer",
    "devops",
    "devops engineer",
    "data engineer",
    "data scientist",
    "machine learning engineer",
    "ai engineer",
    "python developer",
    "javascript developer",
    "react developer",
    "flutter developer",
    "android developer",
    "ios developer",
    "app developer",
    "mobile developer",
    "wordpress developer",
    "cloud engineer",
    "cybersecurity",
    "cyber security",
    "langchain",
    "langgraph",
    "rag developer",
    "api developer",

    # Design no necesariamente video
    "logo designer",
    "logo design",
    "graphic designer",
    "graphic design",
    "illustrator",
    "illustration",
    "vector artist",
    "vector art",
    "ui designer",
    "ux designer",
    "ui/ux designer",
    "ux/ui designer",
    "web designer",
    "website designer",
    "brand designer",
    "branding designer",
    "t-shirt designer",
    "shirt designer",
    "card artist",
    "concept artist",
    "3d artist",
    "character artist",
    "animator",
    "animation artist",

    # Writing / translation
    "writer",
    "copywriter",
    "technical writer",
    "content writer",
    "ghostwriter",
    "translator",
    "translation",
    "proofreader",
    "transcription",
    "transcriber",
    "language tutor",
    "tutor",
    "teacher",
    "french tutor",
    "english tutor",
    "spanish tutor",

    # Business / admin
    "virtual assistant",
    "virtual assistant",
    "data entry",
    "customer support",
    "customer service",
    "technical support",
    "project manager",
    "project coordinator",
    "operations associate",
    "operations manager",
    "account manager",
    "sales representative",
    "sales rep",
    "lead generation",
    "research assistant",
    "administrative assistant",
    "admin assistant",
    "recruiter",
    "recruiting",
    "hr",
    "human resources",

    # Engineering / physical jobs
    "engineer",
    "engineering",
    "technician",
    "automation technician",
    "field service",
    "material planner",
    "mechanical engineer",
    "electrical engineer",
    "civil engineer",

    # Music
    "guitarist",
    "musician",
    "music producer",
    "audio engineer",
    "sound engineer",
    "music editor",
    "songwriter",

    # Other
    "developer",
    "lawyer",
    "accountant",
    "nurse",
    "driver",
    "sales",
    "marketing manager",
]


# ============================================================
# 11. HELPER CONFIG
# ============================================================
# Recomendación para el bot:
#
# Una oferta ideal debería cumplir aproximadamente:
#
#   JOB_KEYWORDS
#       +
#   VIDEO_EDITING_KEYWORDS
#       +
#   REMOTE_KEYWORDS
#       +
#   PAY_KEYWORDS
#
# Y además:
#
#   NOT EXCLUDE_LEVEL
#   NOT EXCLUDE_TOPICS
#   NOT NON_VIDEO_JOB_KEYWORDS
#
# Para español:
#
#   SPANISH_INDICATORS
#
# Para inglés:
#
#   ENGLISH_BASIC_INDICATORS
#
# VALID_LEVEL_KEYWORDS sirve para dar prioridad, no para exigirlo.


# Puntajes sugeridos para un sistema de scoring.
SCORE = {
    "job": 3,
    "video_editing": 5,
    "remote": 3,
    "pay": 3,
    "spanish": 4,
    "english": 2,
    "valid_level": 2,
    "exclude_level": -10,
    "exclude_topic": -8,
    "non_video_job": -10,
}


# Mínimo sugerido para considerar un post candidato.
MIN_SCORE = 8
