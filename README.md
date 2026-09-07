# Implementación de una API REST con autenticación

La empresa necesita una API REST para gestionar usuarios y sus roles. Los usuarios deben poder autenticarse y acceder a recursos protegidos. La API debe manejar la creación, lectura, actualización y eliminación de usuarios, así como la asignación de roles. Los roles determinarán los permisos de acceso a ciertos endpoints.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST con autenticación en Django Rest Framework |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del proyecto y modelo de usuario

**Objetivo:** Configurar el proyecto Django y crear el modelo de usuario con campos de nombre, email y contraseña.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Crear un proyecto Django y configurar el entorno de desarrollo.
- Definir el modelo de usuario con los campos necesarios.
- Asegurar que la contraseña se almacene de forma segura.

**Entregable:** Proyecto Django configurado con modelo de usuario y campo de contraseña seguro.

<details>
<summary>Pistas de conocimiento</summary>

- La configuración inicial del proyecto Django.
- Uso de modelos para definir la estructura de datos.

</details>

### Fase 2: Implementación de la autenticación

**Objetivo:** Implementar la autenticación básica para que los usuarios puedan registrarse y autenticarse.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear las vistas y serializadores necesarios para el registro y autenticación de usuarios.
- Implementar la lógica de autenticación utilizando Django Rest Framework.

**Entregable:** Vistas y serializadores implementados para el registro y autenticación de usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Uso de Django Rest Framework para crear vistas y serializadores.
- Implementación de la lógica de autenticación.

</details>

### Fase 3: Gestión de roles y permisos

**Objetivo:** Implementar la gestión de roles y permisos para controlar el acceso a los endpoints.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear el modelo de rol y asignar roles a los usuarios.
- Implementar la lógica para controlar el acceso a los endpoints basado en los roles de los usuarios.

**Entregable:** Modelo de rol implementado y lógica de control de acceso basada en roles.

<details>
<summary>Pistas de conocimiento</summary>

- Creación y asignación de roles a usuarios.
- Implementación de la lógica de control de acceso.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un modelo de usuario en Django y por qué es necesario?
- **paraQueSirve**: ¿Para qué sirve la autenticación en una API REST y cómo se implementa en Django Rest Framework?
- **comoSeUsa**: ¿Cómo se utiliza Django Rest Framework para crear vistas y serializadores en una API REST?
- **erroresComunes**: ¿Cuáles son los errores comunes durante la implementación de la autenticación y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de la gestión de roles y permisos en una API REST?

## Criterios de Evaluacion

- Proyecto Django configurado con modelo de usuario y campo de contraseña seguro.
- Vistas y serializadores implementados para el registro y autenticación de usuarios.
- Modelo de rol implementado y lógica de control de acceso basada en roles.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
